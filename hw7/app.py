from flask import Flask, request, make_response
from sqlalchemy import create_engine, text
from pymemcache.client.base import Client
from urllib.parse import quote  # To URL-encode the player name
import json


app = Flask(__name__)

@app.route('/hw6')
def hw6(): 
    player = request.args.get('player')
     # connection for MariaDB
    engine = create_engine("mysql+pymysql://root:example@localhost:3306/hw9")
    
    # connection to memcached
    cache = Client('localhost:11211')
    ret = []
    temp = quote(player)
    result = cache.get(temp)
    app.logger.info(f'Cached Result: {result}')
    # if not result: 
    # create a connection cursor
    with engine.connect() as connection:
        result = connection.execute(text("""
                select A.Player as p1,B.Player as p2, C.Player as p3,D.Player as p4 
                from assists A, assists B, assists C, assists D 
                where A.POS=B.POS and B.POS=C.POS and C.POS=D.POS and A.Club<>B.Club and A.club<>C.Club and A.Club<>C.Club and A.Club<>D.Club and B.Club<>C.Club and B.Club<>D.Club and C.Club<>D.Club and A.Player= :player 
                order by A.A+B.A+C.A+D.A desc, A.A desc, B.A desc, C.A desc, D.A desc, p1, p2, p3, p4 limit 1;"""), {"player": player})
        app.logger.info(f"Player received from request: {player}")
        app.logger.info(f"Result: {result}")
        # app.logger.info(f"Result: {result}")
        for row in result:  
            app.logger.info(f"Row: {row}")
            ret = list(row)
        cache.set(temp, ret, 3600)
    resp = make_response({"players": ret}, 200)
    resp.headers["Content-Type"] = "application/json"
    resp.headers["X-CSE356"] = "66cfe2a89ba30e1a6c706759"
    # return the results!
    return resp
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80", debug=True)
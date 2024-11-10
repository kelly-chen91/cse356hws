from flask import Flask, request, make_response
import sqlalchemy
import json

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'example',
    'database': 'hw9'
}

app = Flask(__name__)

@app.route('/hw6')
def hw6(): 
    player = request.args.get('player')
     # connection for MariaDB
    conn = sqlalchemy.connect(**config)
    # create a connection cursor
    cur = conn.cursor()
    # execute a SQL statement
    results = cur.execute(f"""
                select A.Player as p1,B.Player as p2, C.Player as p3,D.Player as p4 
                from assists A, assists B, assists C, assists D 
                where A.POS=B.POS and B.POS=C.POS and C.POS=D.POS and A.Club<>B.Club and A.club<>C.Club and A.Club<>C.Club and A.Club<>D.Club and B.Club<>C.Club and B.Club<>D.Club and C.Club<>D.Club and A.Player=? 
                order by A.A+B.A+C.A+D.A desc, A.A desc, B.A desc, C.A desc, D.A desc, p1, p2, p3, p4 limit 1;""", player)

    return results.first()[0]
    # # serialize results into JSON
    # row_headers=[x[0] for x in cur.description]
    # rv = cur.fetchall()
    # json_data=[]
    # for result in rv:
    #      json_data.append(dict(zip(row_headers,result)))
    # print(cur.)
    

    # return the results!
    # return json.dumps(json_data)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
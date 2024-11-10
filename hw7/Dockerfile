FROM python:3

WORKDIR /usr/src/app

RUN apt update -y
RUN apt install libmariadb3 libmariadb-dev -y

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD [ "python", "app.py"]

FROM python:3

WORKDIR /usr/src/app

RUN sudo apt update -y
RUN sudo apt install libmariadb3 libmariadb-dev -y

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD [ "python", "app.py"]

FROM python:3.9.2 

COPY . /srv/app
WORKDIR /srv/app

EXPOSE 5000

RUN pip3 install -r requirements.txt


 CMD ["python", "app.py"]
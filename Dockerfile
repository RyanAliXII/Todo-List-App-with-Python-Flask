FROM python:3.9.2 

ADD unified/app.py .

EXPOSE 5000

WORKDIR /unified

COPY /unified .

RUN pip3 install -r requirements.txt

CMD ["python", "app.py", "--host=0.0.0.0"]
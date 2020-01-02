FROM ubuntu:18.04
COPY . /app
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 --default-timeout=1000 install django
RUN python3 /app/myproject/manage.py makemigrations
RUN python3 /app/myproject/manage.py migrate --run-syncdb
EXPOSE 8000
CMD ["python3","/app/myproject/manage.py","0.0.0.0","runserver"]

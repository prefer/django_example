FROM ubuntu:15.10
RUN apt-get update
RUN apt-get install -y python-pip
ADD REQUIREMENTS /tmp/REQUIREMENTS
RUN pip install -r /tmp/REQUIREMENTS

ADD . /src
WORKDIR /src
RUN python manage.py migrate
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
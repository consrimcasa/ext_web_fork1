FROM python:3.10-slim-buster

# Set the working directory inside the container
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt



COPY . .


CMD [ "python3", "manage.py", "runserver" ,"0.0.0.0:80"]
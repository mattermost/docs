from python:3

RUN apt-get update

WORKDIR /app

RUN pip3 install pipenv

COPY ./Pipfile .
COPY ./Pipfile.lock .

RUN pipenv install --dev

RUN mkdir -p build/html

COPY . .

FROM python:3

RUN mkdir -p /usr/src/app

RUN apt-get update && apt-get install nodejs npm git -y

WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt

RUN npm install

EXPOSE 8000
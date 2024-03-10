FROM python:alpine

RUN apk add --no-cache nodejs npm

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY ./package.json ./package.json

RUN npm i

COPY . .

EXPOSE 8080

CMD [ "npm", "run", "start" ]
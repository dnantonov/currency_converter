FROM python:3
WORKDIR /code
COPY . .
CMD [ "python", "./server.py" ]
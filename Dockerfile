FROM python:3.11.8

WORKDIR /app

COPY . /app

RUN python -m pip install Flask

CMD [ "python", "./app.py" ]

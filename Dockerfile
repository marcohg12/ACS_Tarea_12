FROM python:3.11.8

WORKDIR /app

COPY . /app

RUN python -m pip install Flask

EXPOSE 5000

CMD [ "python", "./app.py" ]

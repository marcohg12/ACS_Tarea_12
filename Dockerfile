FROM python:3.11.8

WORKDIR /app

COPY . /app

RUN python -m pip install tk

CMD [ "python", "./interface.py" ]

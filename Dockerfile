FROM python:3.11.8

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r tk

CMD [ "python", "./interface.py" ]

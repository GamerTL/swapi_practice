FROM python:3.6-alpine

LABEL maintainer="GamerTL <gamertl001@gmail.com>"

COPY . /swapi_practice

WORKDIR /swapi_practice

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest", "/test/test_sample.py"]
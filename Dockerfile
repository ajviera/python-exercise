FROM python:3.6.3

ENV SRCPATH /usr/src/app
WORKDIR $SRCPATH
RUN apt-get update && pip install --upgrade pip
COPY . $SRCPATH
RUN pip install -r requirements.pip

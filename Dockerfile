FROM python:3.6.3

EXPOSE 8080
ENV SRCPATH /usr/src/app
WORKDIR $SRCPATH
RUN apt-get update && pip install --upgrade pip
COPY . $SRCPATH
RUN pip install -r requirements.pip
CMD [ "python", "src/main.py" ]

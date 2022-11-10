FROM python:3.9

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt-dev \
    libjpeg-dev \
    libfreetype6-dev \
    zlib1g-dev \
    net-tools

ENV HOME=/home/main/
ENV APP_HOME=/home/main/app
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . $APP_HOME

EXPOSE 8000
STOPSIGNAL SIGINT
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

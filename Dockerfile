FROM python:3.11.1


WORKDIR /home/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get clean && apt-get update
RUN apt-get install -y gcc python3-dev python-dev build-essential default-libmysqlclient-dev musl-dev wkhtmltopdf

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y clean && apt-get -y update
RUN apt-get install -y google-chrome-stable
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

ENV XDG_RUNTIME_DIR=/tmp

RUN pip install --upgrade pip --user

COPY code /home/app
RUN pip install -r /home/app/requirements.txt

EXPOSE 8000

RUN #./manage.py collectstatic --noinput
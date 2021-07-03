FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/web
COPY /. .

RUN apt update && apt install wkhtmltopdf -y
RUN pip install --upgrade pip && pip install -r requirements.txt 

RUN chmod a+x /usr/src/web/entrypoint.sh
ENTRYPOINT [ "/usr/src/web/entrypoint.sh" ]
CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000
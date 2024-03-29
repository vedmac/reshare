FROM python:3.9.5-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/web
COPY /. .

RUN apt update && apt install wkhtmltopdf -y \
	&& apt-get autoremove -y && apt-get autoclean -y \
    && pip install poetry \
    && poetry config virtualenvs.create false && poetry install --no-dev

RUN chmod a+x /usr/src/web/entrypoint.sh
ENTRYPOINT [ "/usr/src/web/entrypoint.sh" ]
CMD gunicorn reshare.wsgi:application --bind 0.0.0.0:8000
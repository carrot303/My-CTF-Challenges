FROM python:latest

WORKDIR /app
COPY ./src/ .

ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip && \
	pip install -r requirements.txt

RUN mv flag.txt /flag.txt
ENV FLASK_ENV=development
ENV FLASK_APP=main.py

EXPOSE 1337
CMD ["/app/run.sh"]
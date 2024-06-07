FROM python:latest

WORKDIR /app
COPY ./src/ .

ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip && \
	pip install -r requirements.txt

ENV FLAG=MOTORI{0h_17_w45_pr377y_345Y_r19H7?}
ENV FLASK_ENV=development
ENV FLASK_APP=main.py

EXPOSE 1337
CMD ["/app/run.sh"]
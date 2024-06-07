FROM node

WORKDIR /app
COPY ./src .

RUN npm ci
RUN useradd -m www

COPY flag.txt /flag.txt
RUN chmod 400 /flag.txt
RUN chown www:www /flag.txt

USER www
CMD ["/app/run.sh"]
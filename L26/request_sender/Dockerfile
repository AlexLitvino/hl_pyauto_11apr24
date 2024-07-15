FROM python:3.9

WORKDIR /app

COPY . /app
RUN chmod +x /app/request_sender.py
RUN chmod +x /app/entrypoint.sh

RUN ["pip3", "install", "-r", "requirements.txt"]

ENTRYPOINT ["/app/entrypoint.sh"]
CMD [ "/etc/requests.json" ]
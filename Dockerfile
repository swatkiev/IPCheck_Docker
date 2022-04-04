FROM python:3.9-alpine

RUN pip install requests && pip install pyTelegramBotAPI

WORKDIR /opt/ipbot

COPY run.py /opt/ipbot

CMD ["python", "run.py"]

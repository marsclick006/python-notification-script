FROM python:alpine3.18
COPY app.py app.py
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV REQUEST_URL REQUEST_URL
ENV AUTH AUTH
ENV REQUEST_DATA REQUEST_DATA
ENV WEBHOOK_URL WEBHOOK_URL
ENV ES_URL ES_URL
CMD python3 app.py

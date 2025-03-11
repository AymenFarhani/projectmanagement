FROM python:3.7.3-stretch

ENV PYHTONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

COPY django.sh /app/django.sh

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["/app/django.sh"]

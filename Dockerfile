FROM python:3.8-slim

WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
WORKDIR /usr/src/app/django_falcon
EXPOSE 8000
CMD ["gunicorn", "-c", "gunicorn.conf.py", "-b", "0.0.0.0:8000", "django_falcon.wsgi"]

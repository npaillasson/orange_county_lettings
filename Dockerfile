FROM python:3
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV ENV="PRODUCTION"
RUN  python manage.py collectstatic --noinput
CMD gunicorn orange_county_project.wsgi:application --bind 0.0.0.0:$PORT

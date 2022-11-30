# Dockerfile
FROM python:3.10-slim as common-base
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py collectstatic --no-input
RUN chown -R root /app
RUN sh -c "/app/migrate.sh"
EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]

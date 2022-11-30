#!/bin/bash
cd /app
exec gunicorn --bind '0.0.0.0:8000'  --workers "${GUNICORN_WORKERS:-3}" config.wsgi:application  --worker-tmp-dir /dev/shm
#!/usr/bin/env bash
# Run inside container
cd /app
python manage.py migrate food_info
# exec to replace the shell with uvicorn to handle SIGINT
# ---> Ctrl-C actually exits the container without huge delay
exec uvicorn food_info.asgi:application --host 0.0.0.0
FROM python:3.13-bookworm
STOPSIGNAL SIGINT

RUN apt-get update && apt-get upgrade -y
# TODO: actual db
RUN apt-get update && apt-get install sqlite3 libzbar0 libgl1 -y
ENV PIP_ROOT_USER_ACTION=ignore
RUN python -m pip install --upgrade pip
RUN pip install uvicorn
COPY requirements.txt /
RUN pip install -r requirements.txt
RUN rm requirements.txt

COPY food_info /app
COPY start.sh /app/
WORKDIR /app
ENTRYPOINT ["/app/start.sh"]
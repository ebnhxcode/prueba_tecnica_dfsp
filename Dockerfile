# FROM python:3.10-slim-bullseye
FROM python:3.8-slim-buster

WORKDIR /main

RUN apt update && apt upgrade -y && apt install -y \
  # Booring deps
  sudo curl nmap gcc git bash nano tzdata htop net-tools iputils-ping cron systemd build-essential procps

#RUN find . -type d -name '__pycache__' -exec rm -rf $i {} \;
RUN echo 'alias ll="ls -la"' >> ~/.bashrc
RUN echo 'alias runapp="flask run -p 5555 -h 0.0.0.0"' >> ~/.bashrc
RUN echo 'alias guniapp="gunicorn --bind 0.0.0.0:5555 app:app --reload --workers=1 --threads=1 --log-file=- --worker-tmp-dir /dev/shm --worker-class=gthread"' >> ~/.bashrc



COPY ./main/storage/logs/app.log /main/storage/logs/app.log
RUN ln -sf /proc/1/fd/1 /main/storage/logs/app.log
COPY ./requirements.txt /main


RUN pip install --upgrade pip && pip install -r requirements.txt



#VOLUME main /main
COPY ./main /main

RUN find /main -type d -exec chmod 664 $i {} \;
RUN find /main -type f -exec chmod 775 $i {} \;
RUN chmod -R 777 /main/storage


EXPOSE 5555

# --reload sirve para detectar cambios y recargar el servidor
CMD ["gunicorn", "--bind", "0.0.0.0:5555", "app:app", "--reload", "--workers=2", "--threads=4", "--log-file=-", "--worker-tmp-dir", "/dev/shm" ,"--worker-class=gthread"]
# gunicorn --bind 0.0.0.0:5555 app:app --reload --workers=2 --threads=4 --log-file=- --worker-tmp-dir /dev/shm --worker-class=gthread
# gunicorn --bind 0.0.0.0:5555 app:app --reload --workers=1 --threads=1 --log-file=- --worker-tmp-dir /dev/shm --worker-class=gthread
# gunicorn --bind 0.0.0.0:5555 app:app --reload --workers=1 --threads=4 --log-file=- --worker-tmp-dir /dev/shm --worker-class=gthread

# Este de abajo usar en producción
#CMD ["gunicorn", "--bind", "0.0.0.0:5555", "server:app", "--log-file=-", "--worker-tmp-dir", "/dev/shm", "--workers=8", "--threads=8", "--worker-class=gthread"]

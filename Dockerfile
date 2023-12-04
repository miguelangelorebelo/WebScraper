FROM python:3.10

ENV OPENBLAS_NUM_THREADS=1

RUN python -m pip install --upgrade pip
RUN apt-get update
RUN apt-get install cron -y

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

COPY cronjob /etc/cron.d/cronjob
# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cronjob
RUN crontab /etc/cron.d/cronjob

RUN echo "#!/bin/bash\n"\
         "cron \n"\
         "python main.py"  >> launch.sh
RUN chmod +x launch.sh

ENTRYPOINT ["./launch.sh"]
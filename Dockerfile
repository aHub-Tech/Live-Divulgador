FROM python:3.9-slim-bullseye

LABEL app="livedivulgador"

WORKDIR /app

ADD . .

RUN apt update \
    && apt-get -yy install --no-install-recommends gcc libmariadb-dev \
    && pip3 install -r ./requirements.txt \
    && apt -y remove --purge --auto-remove gcc \
    && apt -y autoremove \
    && apt -y autoclean \
    && apt -y clean \
    && rm -rf /tmp/ \
    && rm -rf /var/lib/apt/lists/ \
    && rm -rf /var/cache/apt/archives/ \
    && pip cache purge \
    && rm -rf /root/.cache/

# CMD [ "python3", "./app/src/bot/main.py" ]

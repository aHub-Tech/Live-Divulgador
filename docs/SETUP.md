# Setup

## Install dependencies

python3 -m venv env

source env/bin/activate

sudo apt install libpq-dev

pip install -r  requirements.txt

### Setup postgres

sudo apt install postgresql -y

sudo service postgresql start

sudo -u postgres createuser livedivulgador

sudo -u postgres createdb streamers

sudo -u postgres psql

alter user livedivulgador with encrypted password 'livedevel123';

grant all privileges on database streamers to livedivulgador;

sudo -u postgres psql streamers < dump.sql

### Startup services

sudo cp exec_live.service /etc/systemd/system/

chmod 775 exec_live.sh

sudo systemctl enable postgresql
sudo systemctl enable exec_live

### Export dump.sql

pg_dump --host localhost \
--port 5432 --username livedivulgador \
--format plain --verbose --file "dump.sql" \
--table public.livecoders streamers

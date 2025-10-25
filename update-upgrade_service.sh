#!/bin/bash

#   work directory
cd /home/ubuntu/my_blog

#   server down
sudo docker-compose -f docker-compose-production.yml down

#   BackUp DB
cp ./data/sqlite/db.sqlite3 /home/ubuntu/configuraciones/backup_db/.

#   Update files
git pull

#   VirtualEnvironment
source ./.venv/bin/activate

#   Static Files
python3 ./my_web/manage.py collectstatic --noinput

#   Make Migrations (DB)
python3 ./my_web/manage.py makemigrations

python3 ./my_web/manage.py migrate

#   Delete old image
image_id=$( sudo docker images | grep my_blog-my_web | awk '{print $3}' )
sudo docker image rm $image_id

#   Restart service
sudo docker-compose -f docker-compose-production.yml up -d


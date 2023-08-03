admin:
	env/bin/python3 manage.py createsuperuser --username admin
migrations:
	env/bin/python3 manage.py makemigrations user registry processo advogado

migrate:
	env/bin/python3 manage.py migrate

build:
	pip install -r requirements.txt
	env/bin/python3 manage.py migrate
	env/bin/python3 manage.py collectstatic --noinput --clear

run:
	env/bin/python3 manage.py runserver

unit_django:
	env/bin/python3 manage.py test

unit_pytest:
	env/bin/python3 manage.py test

celery_connect:
	celery -A project worker --loglevel=INFO

load_data:
	env/bin/python3 manage.py loaddata */fixtures/*.json

run_robot:
	env/bin/python3 manage.py robot

up:
	docker compose -f docker-compose.yml down
	docker compose -f docker-compose.yml up -d

down:
	docker compose -f docker-compose.yml down

coverage:
	coverage run manage.py test
	coverage html

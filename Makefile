admin:
	python manage.py createsuperuser --username admin
migrations:
	python manage.py makemigrations user registry processo advogado

migrate:
	python manage.py migrate

build:
	pip install -r requirements.txt
	python manage.py migrate
	python manage.py collectstatic --noinput --clear

run:
	python manage.py runserver

unit_django:
	python manage.py test

unit_pytest:
	python manage.py test

celery_connect:
	celery -A project worker --loglevel=INFO

load_data:
	python manage.py loaddata */fixtures/*.json

run_robot:
	python manage.py robot

up:
	docker compose -f docker-compose.yml down
	docker compose -f docker-compose.yml up -d

down:
	docker compose -f docker-compose.yml down

coverage:
	coverage run manage.py test
	coverage html

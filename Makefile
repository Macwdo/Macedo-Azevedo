build_image:
	docker build -t macedoazevedoapp:latest .

attach:
	docker attach macedoazevedoapp:latest

admin:
	docker exec -it macedoazevedoapp:latest sh -c 'python manage.py createsuperuser --username admin'

migrations:
	docker exec -i macedoazevedoapp:latest sh -c 'python manage.py makemigrations user cliente parte_adversa processo advogado'

migrate:
	docker exec -i macedoazevedoapp:latest sh -c 'python manage.py migrate'

build:
	docker exec -i macedoazevedoapp:latest sh -c 'pip install -r requirements.txt'
	docker exec -i macedoazevedoapp:latest sh -c 'python manage.py migrate'
	docker exec -i macedoazevedoapp:latest sh -c 'python manage.py collectstatic --noinput --clear'

run:
	docker-compose -f docker-compose.yml down
	docker-compose -f docker-compose.yml up

run_prod:
	docker-compose -f docker-compose-prod.yml down
	docker-compose -f docker-compose-prod.yml up -d

unit:
	docker-compose -f docker-compose.yml run macedoazevedoapp:latest python3 manage.py test

connect:
	docker exec -it macedoazevedoapp:latest /bin/bash

celery_connect:
	docker exec -i macedoazevedoapp:latest sh -c 'celery -A project worker --loglevel=INFO'

load_data:
	docker exec -i macedoazevedoapp:latest sh -c 'python manage.py loaddata */fixtures/*.json'

run_robot:
	docker exec -it macedoazevedoapp:latest python3 manage.py robot

up:
	docker-compose -f docker-compose.yml down
	docker-compose -f docker-compose.yml up -d

down:
	docker-compose -f docker-compose.yml down

coverage:
	docker exec -i macedoazevedoapp:latest sh -c 'coverage run manage.py test'
	docker exec -i macedoazevedoapp:latest sh -c 'coverage html'



build_image:
	docker build -t macedoazevedoapp .

attach:
	docker attach macedoazevedoapp

admin:
	docker exec -it macedoazevedoapp sh -c 'python manage.py createsuperuser --username admin'

migrations:
	docker exec -i macedoazevedoapp sh -c 'python manage.py makemigrations processo advogado cliente'

build:
	docker exec -i macedoazevedoapp sh -c 'pip install -r requirements.txt'
	docker exec -i macedoazevedoapp sh -c 'python manage.py migrate'
	docker exec -i macedoazevedoapp sh -c 'python manage.py collectstatic --noinput --clear'

run:
	docker-compose -f docker-compose.yml down
	docker-compose -f docker-compose.yml up

unit:
	docker exec -i macedoazevedoapp sh -c 'pytest'

connect:
	docker exec -it macedoazevedoapp /bin/bash

celery_connect:
	docker exec -i macedoazevedoapp sh -c 'celery -A project worker --loglevel=INFO'

load_data:
	docker exec -i macedoazevedoapp sh -c 'python manage.py loaddata */fixtures/*.json'

run_robot:
	docker exec -it macedoazevedoapp python3 manage.py robot

up:
	docker-compose -f docker-compose.yml down
	docker-compose -f docker-compose.yml up -d

down:
	docker-compose -f docker-compose.yml down



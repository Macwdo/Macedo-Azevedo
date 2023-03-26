build_image:
	docker build -t macedoazevedoapp .

attach:
	docker attach macedoazevedoapp

admin:
	docker exec -it macedoazevedoapp sh -c 'python manage.py createsuperuser --username admin'

migrations:
	docker exec -i macedoazevedoapp sh -c 'python manage.py makemigrations'

build:
	docker exec -i macedoazevedoapp sh -c 'pip install -r requirements.txt'
	docker exec -i macedoazevedoapp sh -c 'python manage.py migrate'
	docker exec -i macedoazevedoapp sh -c 'python manage.py collectstatic --noinput --clear'

run:
	docker-compose -f docker-compose.yml down
	docker-compose -f docker-compose.yml up


up:
	docker-compose -f docker-compose.yml down
	docker-compose -f docker-compose.yml up -d

down:
	docker-compose -f docker-compose.yml down
build:
	docker-compose build
SVC=
up:
	docker-compose up ${SVC}
down:
	docker-compose down
init:
	touch .env

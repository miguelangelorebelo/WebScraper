clean:
	docker stop EconomistBackend && docker rm EconomistBackend

build:
	docker build -t economist-backend:latest .

run:
	docker run --name=EconomistBackend -d -p 8003:80 economist-backend

connection:
	docker exec -it EconomistBackend bash

watch:
	docker logs -f EconomistBackend
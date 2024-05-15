run: stop
	docker compose build
	docker compose up -d
	docker compose ps
logs:
	docker compose logs user-api
	docker compose logs order-api
stop:
	docker compose down -t 0

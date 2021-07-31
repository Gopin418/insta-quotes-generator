build-and-run:
	docker compose up -d --build
start:
	docker compose up -d
stop:
	docker compose down
logs:
	docker logs -f $(container) --tail 100
restart-backend:
	docker restart quotes_grabber
.PHONY: build
build:
	docker-compose build

.PHONY: up
up: build
	docker-compose up -d

.PHONY: upr
upr: build
	docker-compose up -d --force-recreate

.PHONY: pull
pull:
	docker-compose pull

.PHONY: down
down:
	docker-compose down

# DANGER
.PHONY: dangerous-down
dangerous-down:
	docker-compose down -v

.PHONY: logs
logs:
	docker-compose logs -f

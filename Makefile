NAME=fika
DEBUG_PORT=5201
export PORT = 5200

build: 
	docker build . -t $(NAME) --build-arg port=$(PORT)

stop: 
	docker kill $(NAME)

remove:
	docker rm $(NAME)

restart:
	docker restart $(NAME)

start_docker:
	docker run -dit -p $(PORT):$(PORT) -v $(CURDIR)/config.py:/config.py -v $(CURDIR)/state.json:/state.json -v $(CURDIR)/database.db:/database.db --restart unless-stopped --name $(NAME) $(NAME) 
	
redeploy_docker: stop remove build start_docker

debug:
	gunicorn3 app:app_flask -b 0.0.0.0:$(DEBUG_PORT)


NAME=fika
PORT=5200
DEBUG_PORT=5201

stop: 
	docker kill $(NAME)

remove:
	docker rm $(NAME)

restart:
	docker restart $(NAME)

start_docker:
	docker run -dit -p $(PORT):$(PORT) -v $(CURDIR)/config.py:/config.py -v $(CURDIR)/state.json:/state.json -v $(CURDIR)/database.db:/database.db --restart unless-stopped --name $(NAME) $(NAME) 
	
build:
	docker build . -t $(NAME)

redeploy_docker: stop remove build start_docker

debug:
	gunicorn3 app:app_flask -b 0.0.0.0:$(DEBUG_PORT)


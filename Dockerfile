FROM python:3

WORKDIR /
COPY ./app ./app
COPY requirements.txt .

#RUN apt-get update && apt-get install gunicorn3 -y
RUN pip install --no-cache-dir -r requirements.txt

#CMD ["bash"]
ENV FLASK_RUN_PORT=80
ARG port=5200
ENV PORT=${port}
CMD ["sh", "-c", "gunicorn app:app_flask -b 0.0.0.0:${PORT}"]



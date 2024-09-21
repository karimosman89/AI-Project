install:
	pip install -r requirements.txt

run-flask:
	python src/app.py

docker-build:
	docker build -t ai-project-cifar10 .

docker-run:
	docker-compose up --build

train-model:
	python src/train_model.py

preprocess-images:
	python src/preprocessing.py

start-airflow:
	docker-compose -f airflow/docker-compose.yaml up

test:
	pytest

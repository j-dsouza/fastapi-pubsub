export PUBSUB_EMULATOR_HOST=127.0.0.1:8085

run:
	poetry run uvicorn app.app:app --reload

create-topic:
	poetry run python pubsub.py create-topic test-project test-topic

create-push-subscription:
	poetry run python pubsub.py create-subscription-push test-project test-topic test-subscription "http://localhost:8000/pubsub"

create-messages:
	poetry run python pubsub.py create-message test-project test-topic

import typer
from google.cloud import pubsub_v1

app = typer.Typer()

@app.command()
def create_topic(project_id: str, topic_id: str):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project=project_id, topic=topic_id)

    topic = publisher.create_topic(request={"name": topic_path})

    print(f"Created topic: {topic}")


@app.command()
def create_subscription_push(project_id: str, topic_id: str, subscription_id: str, endpoint: str):
    publisher = pubsub_v1.PublisherClient()
    subscriber = pubsub_v1.SubscriberClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    subscription_path = subscriber.subscription_path(project_id, subscription_id)

    push_config = pubsub_v1.types.PushConfig(push_endpoint=endpoint)

    # Wrap the subscriber in a 'with' block to automatically call close() to
    # close the underlying gRPC channel when done.
    with subscriber:
        subscription = subscriber.create_subscription(
            request={
                "name": subscription_path,
                "topic": topic_path,
                "push_config": push_config,
            }
        )

    print(f"Push subscription created: {subscription}.")
    print(f"Endpoint for subscription is: {endpoint}")


@app.command()
def create_message(project_id: str, topic_id: str):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project=project_id, topic=topic_id)

    for n in range(1, 10):
        data_str = f"Message number {n}"
        # Data must be a bytestring
        data = data_str.encode("utf-8")
        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data)
        print(future.result())

    print(f"Published messages to {topic_path}.")


if __name__ == "__main__":
    app()

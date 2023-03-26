A minimal example of a FastAPI app consuming Google PubSub messages

# Setup

Firstly, set up the pubsub emulator

1. Ensure you have the pubsub emulator installed. See instructions [here](https://cloud.google.com/pubsub/docs/emulator#install_the_emulator)
2. Start the emulator using `gcloud beta emulators pubsub start --project=test-project`

Next, create a new virtualenv and install the python dependencies (this readme assumes you are using poetry)

Once python dependencies are installed, in a new terminal, run the FastAPI app

1. `make run`

Finally, in another terminal use the `pubsub.py` cli to create a topic and subscription, and then begin creating some messages. Examples are in the makefile:

>Note: You must set the environment variable `PUBSUB_EMULATOR_HOST=127.0.0.1:8085` so that the pubsub library knows to connect to the emulator and not a real pubsub instance.

1. `make create-topic`
2. `make create-push-subscription`
3. `make create-messages`

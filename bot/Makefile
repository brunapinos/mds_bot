train-nlu:
	python3 -m rasa_nlu.train -c nlu_config.yml --fixed_model_name current --data data/intents/ -o models --project nlu --verbose

train-core:
	python3 train.py 

train: train-nlu train-core

run-actions:
	python -m rasa_core_sdk.endpoint --actions actions
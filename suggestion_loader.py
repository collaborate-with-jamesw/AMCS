import os
import random
import yaml


SUGGESTIONS_DIR = 'suggestions'


def get_random_suggestion():
    file_list = os.listdir(SUGGESTIONS_DIR)
    suggestion = random.choice(file_list)
    return read_yaml_file_to_dict(
        '{}/{}'.format(SUGGESTIONS_DIR, suggestion)
    )


def read_yaml_file_to_dict(file_path):
    with open(file_path) as suggestion_file:
        return yaml.load(suggestion_file)

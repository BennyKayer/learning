import yaml
from logging import config

with open("logging.yaml", "rt") as f:
    config_data = yaml.safe_load(f.read())
    config.dictConfig(config_data)

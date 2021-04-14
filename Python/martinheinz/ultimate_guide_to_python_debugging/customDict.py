import logging


class MyDict(dict):
    def __missing__(self, key):
        message = f"{key} not present in the dictionary"
        logging.warning(message)
        return message
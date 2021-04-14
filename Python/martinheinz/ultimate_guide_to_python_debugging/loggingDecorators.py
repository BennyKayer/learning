from functools import wraps, partial
import logging


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def log(level, message):
    def decorate(func):
        logger = logging.getLogger(func.__module__)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        log_message = f"{func.__name__} - {message}"

        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.log(level, log_message)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(new_level):
            nonlocal level
            level = new_level

        @attach_wrapper(wrapper)
        def set_message(new_message):
            nonlocal log_message
            log_message = f"{func.__name__} - {new_message}"

        return wrapper

    return decorate


@log(logging.WARN, "example-param")
def somefunc(args):
    return args


somefunc("some args")

somefunc.set_level(logging.CRITICAL)
somefunc.set_message("new-message")
somefunc("some args")

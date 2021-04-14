import logging

logging.basicConfig(
    filename="application.log",
    level=logging.WARNING,
    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)

logging.error("Some serious error occured")
logging.warning("Function you are using is deprecated")
logging.info(logging.getLoggerClass().root.handlers[0].baseFilename)

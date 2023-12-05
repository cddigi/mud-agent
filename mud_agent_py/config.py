import logging
import logging.config
import os
import sys
import time

import dotenv
import yaml

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
dotenv.load_dotenv()


def setup_logging():
    with open("logging.yaml", "r") as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)


def setup():
    setup_logging()

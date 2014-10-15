from rima import server
from tornado.log import logging
from urls import urls_map

logger = logging.getLogger(__name__)
import os
os.environ.setdefault("RIMA_SETTINGS_MODULE", "settings")

if __name__ == '__main__':
	logger.debug("in api")
	server.main(urls_map)
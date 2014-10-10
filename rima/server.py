import logging
 
import tornado.ioloop
import tornado.web
from tornado.web import Application
 
from rima.urls import urls_map

def main():
    settings = {'auto_reload': True, 'debug': True}
    application = Application(urls_map, **settings)
    application.listen(9999)
    logging.info("API server is running on port 9999")
    ioloop_instance = tornado.ioloop.IOLoop.instance()
    ioloop_instance.start()
	

if __name__ == "__main__":
	main()
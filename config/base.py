import json
import tornado.web
import sys
import logging

logger = logging.getLogger('boilerplate.' + __name__)

class Base(tornado.web.RequestHandler):
  """A class to collect common handler methods - all other handlers should
  subclass this one."""
  def set_default_headers(self):
    self.set_header('Content-type', 'text/html; charset=UTF-8')
    self.set_header('Server', 'TornadoServer/4.5.1; Ubuntu; Python')

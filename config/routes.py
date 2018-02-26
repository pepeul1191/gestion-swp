#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from handlers.login import *

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.write('Hello, world???')

routes = [
  (r'/', MainHandler),
  (r'/login', LoginIndex),
]

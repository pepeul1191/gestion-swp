#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from config.constants import constants
from config.base import BaseHandler

class LoginIndex(BaseHandler):
  def get(self):
    self.set_status(200)
    self.render('handlers/login.html', constants= constants, title= 'Login', data= 'false')

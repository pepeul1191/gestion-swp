#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from config.base import BaseHandler

class LoginIndex(BaseHandler):
  def get(self):
    self.set_status(400)
    self.render('handlers/login.html', title='Login')

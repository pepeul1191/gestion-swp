#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from config.constants import constants
from config.base import BaseHandler

class HomeIndex(BaseHandler):
  def get(self):
    if self.get_secure_cookie('estado'):
      if self.get_secure_cookie('estado').decode("utf-8") != 'activo':
        self.redirect('/login')
      else:
        self.render('handlers/home.html', constants= constants, title= 'Home', data= False)
    else:
      self.redirect('/login')
       #TODO cuando el estado del usuario exista pero no sea 'activo'

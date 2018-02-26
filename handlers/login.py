#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import requests
import datetime
from config.constants import constants
from config.base import BaseHandler

class LoginIndex(BaseHandler):
  def get(self):
    self.set_status(200)
    self.render('handlers/login.html', constants= constants, title= 'Login', data= False)

class LoginAcceder(BaseHandler):
  def post(self):
    usuario = self.get_argument('usuario')
    contrasenia =  self.get_argument('contrasenia')
    url = constants['servicios']['accesos'] + 'usuario/acceder?usuario=' + usuario + '&contrasenia=' + contrasenia
    response = requests.post(url)
    if response.text == '1':
      self.set_secure_cookie('usuario', usuario)
      self.set_secure_cookie('tiempo', str(datetime.datetime.now()))
      self.redirect('/')
      return
    else:
      self.render('handlers/login.html', constants= constants, title= 'Login', data= True)
      return

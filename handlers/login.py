#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import requests
import datetime
import json
from config.base import Base

class LoginIndex(Base):
  def set_default_headers_nuevo(self):
    print('set_default_headers!!!!!!!!!!!!!!!!!!!!!')
    self.set_header("Access-Control-Allow-Origin", "*")

  def get(self):
    self.set_default_headers_nuevo()
    self.set_status(400)
    self.write("<h1>LOGIN</h1>")

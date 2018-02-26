#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import requests
import datetime
import json
from config.base import BaseHandler

class LoginIndex(BaseHandler):
  def get(self):
    self.set_status(400)
    self.write("<h1>LOGIN</h1>")

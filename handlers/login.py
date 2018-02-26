#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import requests
import datetime
import json
from config.base import Base
from config.middleware import enable_cors

class LoginIndex(Base):
  @enable_cors()
  def get(self):
    self.set_status(400)
    self.write("<h1>LOGIN</h1>")

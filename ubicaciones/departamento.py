#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import requests
import datetime
import json
from sqlalchemy.sql import select
from config.database import engine
from config.base import BaseHandler
from config.middleware import enable_cors
from .models import Departamento

class UbicacionesDepartamentoListar(BaseHandler):
  @enable_cors()
  def get(self):
    conn = engine.connect()
    stmt = select([Departamento])
    return self.write(json.dumps([dict(r) for r in conn.execute(stmt)]))

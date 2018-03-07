#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import requests
import datetime
import json
from sqlalchemy.sql import select
from config.database import engine_ubicaciones
from config.base import BaseHandler
from config.middleware import enable_cors
from .models import Provincia

class UbicacionesProvinciaListar(BaseHandler):
  @enable_cors()
  def get(self, departamento_id):
    conn = engine_ubicaciones.connect()
    stmt = select([Provincia]).where(Provincia.departamento_id == departamento_id)
    return self.write(json.dumps([dict(r) for r in conn.execute(stmt)]))

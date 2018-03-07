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
from .models import Distrito

class UbicacionesDistritoListar(BaseHandler):
  @enable_cors()
  def get(self, provincia_id):
    conn = engine_ubicaciones.connect()
    stmt = select([Distrito]).where(Distrito.provincia_id == provincia_id)
    return self.write(json.dumps([dict(r) for r in conn.execute(stmt)]))

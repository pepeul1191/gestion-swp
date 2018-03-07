#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import requests
import datetime
import json
from sqlalchemy.sql import select
from config.database import engine_ubicaciones, session_ubicaciones
from config.base import BaseHandler
from config.middleware import enable_cors
from .models import Departamento

class UbicacionesDepartamentoListar(BaseHandler):
  @enable_cors()
  def get(self):
    conn = engine_ubicaciones.connect()
    stmt = select([Departamento])
    return self.write(json.dumps([dict(r) for r in conn.execute(stmt)]))

class UbicacionesDepartamentoGuardar(BaseHandler):
  @enable_cors()
  def post(self):
    data = json.loads(self.get_argument('data'))
    nuevos = data['nuevos']
    editados = data['editados']
    eliminados = data['eliminados']
    pais_id = data['extra']['pais_id']
    array_nuevos = []
    rpta = None
    session = session_ubicaciones()
    try:
      if len(nuevos) != 0:
        for nuevo in nuevos:
          temp_id = nuevo['id']
          nombre = nuevo['nombre']
          s = Departamento(nombre = nombre, pais_id = pais_id)
          session.add(s)
          session.flush()
          temp = {'temporal' : temp_id, 'nuevo_id' : s.id}
          array_nuevos.append(temp)
      if len(editados) != 0:
        for editado in editados:
          session.query(Departamento).filter_by(id = editado['id']).update(editado)
      if len(eliminados) != 0:
        for id in eliminados:
          session.query(Departamento).filter_by(id = id).delete()
      session.commit()
      rpta = {'tipo_mensaje' : 'success', 'mensaje' : ['Se ha registrado los cambios en los departamentos', array_nuevos]}
    except Exception as e:
      session.rollback()
      rpta = {'tipo_mensaje' : 'error', 'mensaje' : ['Se ha producido un error en guardar los departamentos', str(e)]}
    return self.write(json.dumps(rpta))
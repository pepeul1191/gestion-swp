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
from .models import Distrito, VWDistritoProvinciaDepartamento as VW

class UbicacionesDistritoListar(BaseHandler):
  @enable_cors()
  def get(self, provincia_id):
    conn = engine_ubicaciones.connect()
    stmt = select([Distrito]).where(Distrito.provincia_id == provincia_id)
    return self.write(json.dumps([dict(r) for r in conn.execute(stmt)]))

class UbicacionesDistritoBuscar(BaseHandler):
  @enable_cors()
  def get(self):
    distrito = self.get_argument('distrito')
    session = session_ubicaciones()
    rs = session.query(VW).filter(VW.nombre.like(distrito + '%')).limit(10).all()
    rpta = []
    for distrito in rs:
      t = {'id': distrito.id, 'nombre': distrito.nombre}
      rpta.append(t)
    return self.write(json.dumps(rpta))

class UbicacionesDistritoGuardar(BaseHandler):
  @enable_cors()
  def post(self):
    data = json.loads(self.get_argument('data'))
    nuevos = data['nuevos']
    editados = data['editados']
    eliminados = data['eliminados']
    provincia_id = data['extra']['provincia_id']
    array_nuevos = []
    rpta = None
    session = session_ubicaciones()
    try:
      if len(nuevos) != 0:
        for nuevo in nuevos:
          temp_id = nuevo['id']
          nombre = nuevo['nombre']
          s = Distrito(nombre = nombre, provincia_id = provincia_id)
          session.add(s)
          session.flush()
          temp = {'temporal' : temp_id, 'nuevo_id' : s.id}
          array_nuevos.append(temp)
      if len(editados) != 0:
        for editado in editados:
          session.query(Distrito).filter_by(id = editado['id']).update(editado)
      if len(eliminados) != 0:
        for id in eliminados:
          session.query(Distrito).filter_by(id = id).delete()
      session.commit()
      rpta = {'tipo_mensaje' : 'success', 'mensaje' : ['Se ha registrado los cambios en los distritos', array_nuevos]}
    except Exception as e:
      session.rollback()
      rpta = {'tipo_mensaje' : 'error', 'mensaje' : ['Se ha producido un error en guardar los distritos', str(e)]}
    return self.write(json.dumps(rpta))
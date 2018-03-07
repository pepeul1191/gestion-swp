#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from handlers.login import LoginIndex, LoginAcceder, LoginEstado, LoginSalir
from handlers.home import HomeIndex
from ubicaciones.departamento import *
from ubicaciones.provincia import *
from ubicaciones.distrito import *

routes = [
  (r'/', HomeIndex),
  (r'/login', LoginIndex),
  (r'/login/acceder', LoginAcceder),
  (r'/usuario/ver', LoginEstado),
  (r'/usuario/salir', LoginSalir),
  # ubicaciones
  (r'/ubicaciones/departamento/listar', UbicacionesDepartamentoListar),
  (r'/ubicaciones/departamento/guardar', UbicacionesDepartamentoGuardar),
  (r'/ubicaciones/distrito/listar/([0-9]+)', UbicacionesDistritoListar),
  (r'/ubicaciones/distrito/buscar', UbicacionesDistritoBuscar),
  (r'/ubicaciones/distrito/guardar', UbicacionesDistritoGuardar),
  (r'/ubicaciones/provincia/listar/([0-9]+)', UbicacionesProvinciaListar),
  (r'/ubicaciones/provincia/guardar', UbicacionesProvinciaGuardar),
]

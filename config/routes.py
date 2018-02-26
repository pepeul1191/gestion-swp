#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from handlers.login import LoginIndex, LoginAcceder
from handlers.home import HomeIndex
from ubicaciones.departamento import *

routes = [
  (r'/', HomeIndex),
  (r'/login', LoginIndex),
  (r'/login/acceder', LoginAcceder),
  (r'/ubicaciones/departamento/listar', UbicacionesDepartamentoListar),
]

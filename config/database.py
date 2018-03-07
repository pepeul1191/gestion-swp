# config/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
# Base de datos sql relacional - ubicaciones
engine_ubicaciones = create_engine('sqlite:///db/ubicaciones.db')
session_ubicaciones = sessionmaker()
session_ubicaciones.configure(bind = engine_ubicaciones)
# Base de datos sql relacional - accesos
engine_accesos = create_engine('sqlite:///db/db_accesos.db')
session_accesos = sessionmaker()
session_accesos.configure(bind = engine_accesos)

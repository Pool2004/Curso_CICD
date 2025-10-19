from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# URL de conexión (se obtiene de variables de entorno)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:12345@db:5432/gestor_tareas")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    descripcion = Column(String(500))
    prioridad = Column(String(50), default="media")
    fecha_vencimiento = Column(String(50))
    completada = Column(Boolean, default=False)
    creada_en = Column(DateTime, default=datetime.now)

# Crear las tablas
def init_db():
    Base.metadata.create_all(bind=engine)

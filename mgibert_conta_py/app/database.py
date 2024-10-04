from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://pablo:example@localhost:5433/treasury")

# Crear un motor asíncrono con SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Crear una sesión asíncrona
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Dependencia para obtener la sesión de la base de datos
def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

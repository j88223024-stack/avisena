from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import Optional
import logging

from app.schemas.finca import FincaCreate

logger = logging.getLogger(__name__)

def create_finca(db: Session, finca: FincaCreate) -> Optional[bool]:
    try:
        sentencia = text("""
            INSERT INTO fincas (
                nombre, longitud, latitud,
                id_usuario, estado
            ) VALUES (
                :nombre, :longitud, :latitud,
                :id_usuario, :estado
            )
        """)
        db.execute(sentencia, finca.model_dump())
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        logger.error(f"Error al crear finca: {e}")
        raise Exception("Error de base de datos al crear la finca")

    
def get_finca_by_id(db: Session, id: int):
    try:
        query = text("""SELECT fincas.id_finca,  fincas.nombre, fincas.longitud, fincas.latitud,
                            usuarios.nombre as nombre_usuario, fincas.estado
                        FROM fincas INNER JOIN usuarios ON fincas.id_usuario = usuarios.id_usuario
                        WHERE id_finca = :id_finca""")
        result = db.execute(query, {"id_finca": id}).mappings().first()
        return result
    except Exception as e:
        logger.error(f"Error al obtener la finca por id: {e}")
        raise Exception("Error de base de datos al obtener la finca")
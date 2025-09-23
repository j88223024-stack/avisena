from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.router.dependencies import get_current_user
from core.database import get_db
from app.schemas.finca import FincaCreate, FincaUpdate, FincaOut
from app.crud import finca as crud_finca

router2 = APIRouter()

@router2.post("/crear", status_code=status.HTTP_201_CREATED)
def create_finca(
    finca: FincaCreate, 
    db: Session = Depends(get_db)
):
    try:
        crud_finca.create_finca(db, finca)
        return {"message": "Finca creado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
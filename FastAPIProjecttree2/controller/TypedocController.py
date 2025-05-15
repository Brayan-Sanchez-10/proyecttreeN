from fastapi import APIRouter, HTTPException
from service.typedocService import TypedocService

router = APIRouter(prefix="/typedocs", tags=["TypeDocs"])
typedoc_service = TypedocService()


@router.get("/")
def get_all_typedocs():
    docs = typedoc_service.get_all()
    if not docs:
        raise HTTPException(status_code=404, detail="No hay tipos de documento disponibles.")
    return docs
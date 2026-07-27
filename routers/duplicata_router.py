from fastapi import APIRouter, HTTPException
from schemas.duplicata_schema import *
from services.duplicata_services import DuplicataService

duplicata_router = APIRouter(prefix="/duplicata", tags=["duplicata"])

@duplicata_router.post("/valida", response_model=DuplicataResponse)
async def valida_duplicata(duplicata_request: DuplicataRequest):

    try:
        valida = DuplicataService.valida(duplicata_request.pk, duplicata_request.dados)
        return {
            "chave_pk": duplicata_request.pk,
            "qtde_duplicata": valida,
            "validacao": "Dados processados com sucesso"
        }
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
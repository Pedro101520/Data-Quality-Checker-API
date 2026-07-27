from fastapi import APIRouter
from schemas.duplicata_schema import *
from services.duplicata_services import DuplicataService

duplicata_router = APIRouter(prefix="/duplicata", tags=["duplicata"])

@duplicata_router.post("/valida", response_model=DuplicataResponse)
async def valida_duplicata(duplicata_request: DuplicataRequest):

    valida = DuplicataService.valida(duplicata_request.pk, duplicata_request.dados)

    return {
        "chave_pk": duplicata_request.pk,
        "qtde_duplicata": valida
    }
from fastapi import APIRouter
from schemas.cnpj_schema import CnpjRequest, CnpjResponse
from services.cnpj_services import CnpjService

cnpj_router = APIRouter(prefix="/cnpj", tags=["cnpj"])

@cnpj_router.get("/")
async def home():
    return {"mensagem": "Voce acessou a rota padrao de autenticacao", "autenticacao": False}

@cnpj_router.post("/valida", response_model=CnpjResponse)
async def valida_cnpj(cnpj_request: CnpjRequest):

    valido = CnpjService.validaCnpj(cnpj_request.cnpj)

    return {
        "cnpj": cnpj_request.cnpj,
        "valido": valido["valido"],
        "motivo": valido["motivo"]
    }
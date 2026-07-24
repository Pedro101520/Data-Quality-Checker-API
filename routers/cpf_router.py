from fastapi import APIRouter
from schemas.cpf_schema import CpfRequest, CpfResponse
from services.cpf_services import CpfService

cpf_router = APIRouter(prefix="/cpf", tags=["cpf"])

@cpf_router.post("/valida", response_model=CpfResponse)
async def valida_cpf(cpf_request: CpfRequest):

    valido = CpfService.validaCpf(cpf_request.cpf)

    return {
        "cpf": cpf_request.cpf,
        "valido": valido["valido"],
        "motivo": valido["motivo"]
    }
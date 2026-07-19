from pydantic import BaseModel

class CpfRequest(BaseModel):
    cpf: str

class CpfResponse(BaseModel):
    cpf: str
    valido: bool
    motivo: str
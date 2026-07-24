from pydantic import BaseModel

class CnpjRequest(BaseModel):
    cnpj: str

class CnpjResponse(BaseModel):
    cnpj: str
    valido: bool
    motivo: str
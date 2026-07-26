from pydantic import BaseModel, Field
from typing import Any

class DuplicataRequest(BaseModel):
    pk: str = Field(description="Valor de referência para conferir duplicatas")
    dados: list[dict[str, Any]] = Field(
        description="Lista de valores a ser informada",
        examples=[[
            {"cnpj": "12345678000190", "nome": "Empresa A"},
            {"cnpj": "12345678000190", "nome": "Empresa A Ltda"},
        ]]
    )


class ValoresDuplicataResponse(BaseModel):
    chave: str
    num_ocorrencia: int

class DuplicataResponse(BaseModel):
    duplicados: list[ValoresDuplicataResponse]
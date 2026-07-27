from pydantic import BaseModel, Field
from typing import Any

class DuplicataRequest(BaseModel):
    pk: str = Field(description="Valor de referência para conferir duplicatas")
    dados: list[dict[str, Any]] = Field(
        {
            "pk": "cpf",
            "dados": [
                {
                "id": 1,
                "nome": "Pedro",
                "idade": 25,
                "cidade": "São Paulo"
                }
            ]
        }
    )


class ValoresDuplicataResponse(BaseModel):
    chave: str
    num_ocorrencia: int

class DuplicataResponse(BaseModel):
    chave_pk: str
    qtde_duplicata: int
    validacao: str
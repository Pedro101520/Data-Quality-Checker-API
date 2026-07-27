from services.duplicata_services import DuplicataService
import pytest

import pytest
from services.duplicata_services import DuplicataService

def test_pk_diferente():
    with pytest.raises(
        ValueError,
        match="Pk não encontrada nos dados disponibilizados"
    ):
        DuplicataService.valida(
            "cpf",
            [
                {
                    "id": 1,
                    "nome": "Pedro",
                    "idade": 25,
                    "cidade": "São Paulo"
                }
            ]
        )


@pytest.mark.parametrize(
    "pk, dados, retorno_esperado",
    [
        (
            "id",
            [
                {
                    "id": 1,
                    "nome": "Pedro",
                    "idade": 25,
                    "cidade": "São Paulo"
                },
                {
                    "id": 1,
                    "nome": "Pedro",
                    "idade": 25,
                    "cidade": "São Paulo"
                }
            ],
            1
        )
    ]
)
def test_valores_duplicados(pk, dados, retorno_esperado):
    verifica = DuplicataService.valida(pk, dados)

    assert verifica == retorno_esperado


@pytest.mark.parametrize(
    "pk, dados, retorno_esperado",
    [
        (
            "id",
            [
                {
                    "id": 1,
                    "nome": "Pedro",
                    "idade": 25,
                    "cidade": "São Paulo"
                },
                {
                    "id": 2,
                    "nome": "Pedro",
                    "idade": 25,
                    "cidade": "São Paulo"
                }
            ],
            0
        )
    ]
)
def test_valores(pk, dados, retorno_esperado):
    verifica = DuplicataService.valida(pk, dados)

    assert verifica == retorno_esperado
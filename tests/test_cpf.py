from services.cpf_services import CpfService
import pytest

def test_cpf_dig_iguais():
    verifica = CpfService.validaCpf("111.111.111-11")

    assert verifica == {
        "valido": False,
        "motivo": "CPF inválido"
    }

@pytest.mark.parametrize("cpf, retorno_esperado", 
                         [("abs.567.o60-10", {"valido": False,"motivo": "CPF inválido"}), ("ahn.erk.opl-wn", {"valido": False,"motivo": "CPF inválido"})])
def test_cpf_caracter(cpf, retorno_esperado):
    verifica = CpfService.validaCpf(cpf)

    assert verifica == retorno_esperado


def test_cpf_valido():
    verifica = CpfService.validaCpf("286.255.878-87")

    assert verifica == {
        "valido": True,
        "motivo": "CPF válido"
    }

def test_cpf_invalido():
    verifica = CpfService.validaCpf("286.255.878-80")

    assert verifica == {
        "valido": False,
        "motivo": "CPF inválido"
    }

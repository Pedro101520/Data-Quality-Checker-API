from services.cnpj_services import CnpjService
import pytest

def test_cnpj_dig_iguais():
    verifica = CnpjService.validaCnpj("00000000000000")

    assert verifica == {
        "valido": False,
        "motivo": "CNPJ inválido"
    }

@pytest.mark.parametrize("cnpj, retorno_esperado", 
                         [("k9.p34.y6n/3wd2-60", {"valido": False,"motivo": "CNPJ inválido"}), ("RQ.4F5.ZR3/7E3P-19", {"valido": False,"motivo": "CNPJ inválido"}), ("E2Z8IQ9Y7JZB04", {"valido": False,"motivo": "CNPJ inválido"})])
def test_cnpj_alfanumerico_invalido(cnpj, retorno_esperado):
    verifica = CnpjService.validaCnpj(cnpj)

    assert verifica == retorno_esperado


@pytest.mark.parametrize("cnpj, retorno_esperado", 
                         [("po.cbe.f85/goxy-72", {"valido": True,"motivo": "CNPJ válido"}), ("5VCQDNOD9TBL88", {"valido": True,"motivo": "CNPJ válido"}), ("5X.5UK.P2H/Z0RD-40", {"valido": True,"motivo": "CNPJ válido"})])
def test_cnpj_alfanumerico_valido(cnpj, retorno_esperado):
    verifica = CnpjService.validaCnpj(cnpj)
    assert verifica == retorno_esperado

@pytest.mark.parametrize("cnpj, retorno_esperado", 
                         [("69.747.045/8739-80", {"valido": False,"motivo": "CNPJ inválido"}), ("95068689786553", {"valido": False,"motivo": "CNPJ inválido"})])
def test_cnpj_numerico_invalido(cnpj, retorno_esperado):
    verifica = CnpjService.validaCnpj(cnpj)

    assert verifica == retorno_esperado


@pytest.mark.parametrize("cnpj, retorno_esperado", 
                         [("04.164.106/8855-15", {"valido": True,"motivo": "CNPJ válido"}), ("02258532061964", {"valido": True,"motivo": "CNPJ válido"})])
def test_cnpj_numerico_valido(cnpj, retorno_esperado):
    verifica = CnpjService.validaCnpj(cnpj)

    assert verifica == retorno_esperado
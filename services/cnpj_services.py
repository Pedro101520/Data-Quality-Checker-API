import re
import json

class CnpjService:

    @staticmethod
    def validaCnpj(cnpj):
        cnpj_limpo = re.sub(r'[^a-zA-Z0-9]', '', cnpj)

        if len(cnpj_limpo) == 14:
            cnpj_maiusculo = cnpj_limpo.upper()
            if not(len(set(cnpj_maiusculo))) <= 1:
                try:
                    int(cnpj_maiusculo[12:14])
                except:
                    return {
                        "valido": False, 
                        "motivo": "CNPJ inválido"
                    }   

                with open("assets//ASCII_letra.json", "r", encoding="utf-8") as arquivo:
                    valores = json.load(arquivo)

                lista_numerica = []
                for i in cnpj_maiusculo:
                    try:
                        lista_numerica.append(int(i))
                    except:
                        num_ascii = valores[i]
                        lista_numerica.append(num_ascii)

                pesos_fixos = [5,4,3,2,9,8,7,6,5,4,3,2]
                dig_1 = 0
                soma_dig_1 = 0
                for peso, dig_cnpj in zip(pesos_fixos, lista_numerica[0:12]):
                    soma_dig_1 += (peso * dig_cnpj)

                resto_divisao_dig_1 = soma_dig_1 % 11
                if resto_divisao_dig_1 < 2:
                    dig_1 = 0
                else:
                    dig_1 = 11 - resto_divisao_dig_1


                pesos_fixos = [6,5,4,3,2,9,8,7,6,5,4,3]
                dig_2 = 0
                soma_dig_2 = 0
                for peso, dig_cnpj in zip(pesos_fixos, lista_numerica[0:12]):
                    soma_dig_2 += (peso * dig_cnpj)

                soma_dig_2 += (dig_1 * 2)

                resto_divisao_dig_2 = soma_dig_2 % 11
                if resto_divisao_dig_2 < 2:
                    dig_2 = 0
                else:
                    dig_2 = 11 - resto_divisao_dig_2


                if int(cnpj_maiusculo[12:14]) == int(f"{dig_1}{dig_2}"):
                    return {
                        "valido": True,
                        "motivo": "CNPJ válido"
                    }
                else:
                    return {
                        "valido": False,
                        "motivo": "CNPJ inválido"
                    }
                  
            else:
                return {
                    "valido": False, 
                    "motivo": "CNPJ inválido"
                }
        else:
            return {
                "valido": False,
                "motivo": "CNPJ inválido"
            }
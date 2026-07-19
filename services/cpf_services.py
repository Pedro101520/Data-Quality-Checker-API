import re

class CpfService:

    @staticmethod
    def validaCpf(cpf):
        cpf_limpo = re.sub(r'\D', '', cpf)

        estrutura_calculo = cpf_limpo[0:9]

        conta_primeiro_dig = 10
        operacao_primeiro_dig = 0

        conta_segundo_dig = 11
        operacao_segundo_dig = 0

        if len(cpf_limpo) == 11 and not(len(set(cpf_limpo)) <= 1):
            for i in estrutura_calculo:
                if conta_primeiro_dig >= 2:
                    operacao_primeiro_dig += int(i) * conta_primeiro_dig
                    conta_primeiro_dig -= 1
                
            operacao_primeiro_dig = (operacao_primeiro_dig * 10) % 11

            if operacao_primeiro_dig == 10:
                operacao_primeiro_dig = 0
            
            for j in estrutura_calculo:
                if conta_segundo_dig >= 3:
                    operacao_segundo_dig += int(j) * conta_segundo_dig
                    conta_segundo_dig -= 1
            
            operacao_segundo_dig = ((operacao_segundo_dig + (operacao_primeiro_dig * 2)) * 10) % 11

            if operacao_segundo_dig == 10:
                operacao_segundo_dig = 0

            if f"{operacao_primeiro_dig}{operacao_segundo_dig}" == cpf_limpo[9:11]:
                return {
                    "valido": True, 
                    "motivo": "CPF válido"
                }
            else:
                return {
                    "valido": False,
                    "motivo": "CPF inválido"
                }
                 
        else:
            return {
                "valido": False, 
                "motivo": "CPF inválido"
            }

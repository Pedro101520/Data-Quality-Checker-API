# Projeto Data Quality Checker

O objetivo deste projeto foi principalmente para aprimorar minhas habilidades com pipelines CI/CD, por este motivo a API que desenvolvi foi simples, pois este repositório foi pensado em criar algo de base para que eu pudesse aprender sobre pipelines automatizadas

---

## Tecnologias utilizadas
- Python
- FastAPI
- Pandas
- Pytest
- AWS (ECR, Lambda)
- CI/CD
- Docker

---

## Rodando localmente
```
# Clonar o repositório
git clone https://github.com/Pedro101520/Data-Quality-Checker-API.git

# Executando localmente a API
python -m venv venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
```

A API sobe em http://127.0.0.1:8000. Documentação interativa (Swagger) disponível em http://127.0.0.1:8000/docs.

---

## Rodando os testes unitários
```
pytest -v
```

---

## Endpoints

### default
```
/
```
Usado para testar se a API está no ar

### CPF
```
/cpf/valida
```
Verifica se um CPF é válido ou não

### CNPJ
```
/cnpj/valida
```
Verifica se um CNPJ é válido ou não (Já inclui a verificação com CNPJ alfanumérico)

### duplicata
```
/duplicata/valida
```
Retorna o número de informações duplicatas em uma lista de JSON com base na chave primária indicada pelo usuário

---

## Pipeline de CI/CD

## CI
Na etapa de CI, inclui:
- Verificações de trigger quando ocorrer push nas branches feature/* ou na main
- Pull request na branch main
- Após a ativação, ocorre o build do ambiente, preparando a máquina e instalando as bibliotecas com base no requirements.txt
- Verificação por meio de testes unitários usando o pytest

## CD
- Configurei as credenciais de forma segura da AWS por meio do Repository secrets do github
- Build da imagem docker e push no serviço AWS ECR
- Deploy no AWS Lambda

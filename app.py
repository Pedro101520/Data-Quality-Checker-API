from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

from routers.cpf_router import cpf_router
from routers.cnpj_router import cnpj_router
from routers.health_route import health_route

app.include_router(health_route)
app.include_router(cpf_router)
app.include_router(cnpj_router)

# Opcao para configurar o AWS lambda
handler = Mangum(app)
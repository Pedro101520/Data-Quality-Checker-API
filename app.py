from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

from routers.cpf import cpf_router

app.include_router(cpf_router)

# Opcao para configurar o AWS lambda
handler = Mangum(app)
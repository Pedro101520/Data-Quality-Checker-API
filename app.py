from fastapi import FastAPI

app = FastAPI()

from routers.cpf import cpf_router

app.include_router(cpf_router)
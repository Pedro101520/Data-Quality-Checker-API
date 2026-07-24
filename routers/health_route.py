from fastapi import APIRouter

health_route = APIRouter(prefix="/")

@health_route.get("/")
async def home():
    return {"mensagem": "Voce acessou a rota padrao de autenticacao", "autenticacao": False}
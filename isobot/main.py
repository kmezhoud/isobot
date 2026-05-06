from fastapi import FastAPI
from isobot.api.routes_docs import router as docs_router
from fastapi.responses import HTMLResponse

# D'abord créer l'application
isobot = FastAPI(title="ISOBOT")

# Ensuite définir les routes
@isobot.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>Bienvenue dans ISOBOT</h1>
    <p>Robot ISO 9001 opérationnel</p>
    <a href="/docs">Swagger UI</a>
    """

# Ensuite ajouter les routers
isobot.include_router(docs_router, prefix="/documents")

#isobot.include_router(docs_router, prefix="/docs", tags=["Documents"])

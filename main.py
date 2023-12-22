#main.py
from fastapi import FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from repositories.ProdutoRepo import ProdutoRepo

# IMPORTAÇÕES DA PASTA ROUTER
from routes.RootRouter import router as rootRouter
from routes.LeggedRouter import router as leggedRouter
from routes.PlayRouter import router as playRouter
from routes.InfoVideosRouter import router as infoVideosRouter
from routes.InfoVideosLeggedRouter import router as infoVideosLeggedRouter
from routes.ProdutoRouter import router as produtoRouter

# CRIAR TABELAS
ProdutoRepo.criar_tabela()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")

app.include_router(rootRouter)
app.include_router(leggedRouter)
app.include_router(playRouter)
app.include_router(infoVideosRouter)
app.include_router(infoVideosLeggedRouter)
app.include_router(produtoRouter)

if __name__ == "__main__":
   uvicorn.run(app="main:app", reload=True)
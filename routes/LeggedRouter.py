#main.py
from fastapi import APIRouter, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# CORPO DO SITE PASTA LEGGED
@router.get("/index_legged")
def getroot(request: Request):
        return templates.TemplateResponse("legged/index_legged.html", {"request": request})

@router.get("/perfil")
def getroot(request: Request):
        return templates.TemplateResponse("legged/perfil.html", {"request": request})


@router.get("/desenvolvimento_legged")
def getroot(request: Request):
        return templates.TemplateResponse("legged/desenvolvimento_legged.html", {"request": request})

@router.get("/add_perfil")
def getroot(request: Request):
        return templates.TemplateResponse("legged/add_perfil.html", {"request": request})

@router.get("/alt_perfil")
def getroot(request: Request):
        return templates.TemplateResponse("legged/alt_perfil.html", {"request": request})

@router.get("/excluir")
def getroot(request: Request):
        return templates.TemplateResponse("legged/excluir.html", {"request": request})
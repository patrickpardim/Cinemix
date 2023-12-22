#main.py
from fastapi import APIRouter, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# INFORMAÇÕES FILMES LEGGED
@router.get("/info_videos_legged/info_noite_bruxas")
def getDados(request: Request):
        return templates.TemplateResponse("/info_videos_legged/info_noite_bruxas.html", {"request": request})

@router.get("/info_videos_legged/info_wanda_vision")
def getDados(request: Request):
        return templates.TemplateResponse("/info_videos_legged/info_wanda_vision.html", {"request": request})

@router.get("/info_videos_legged/info_insidius")
def getDados(request: Request):
        return templates.TemplateResponse("/info_videos_legged/info_insidius.html", {"request": request})

@router.get("/info_videos_legged/info_morte_demonio")
def getDados(request: Request):
        return templates.TemplateResponse("/info_videos_legged/info_morte_demonio.html", {"request": request})

@router.get("/info_videos_legged/info_transformes")
def getDados(request: Request):
        return templates.TemplateResponse("/info_videos_legged/info_transformes.html", {"request": request})
#main.py
from fastapi import APIRouter, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# PLAY DE VIDEOS
@router.get("/play_videos/pantera_negra")
def getDados(request: Request):
        return templates.TemplateResponse("/play_videos/pantera_negra.html", {"request": request})

@router.get("/play_videos/wanda_vision")
def getDados(request: Request):
        return templates.TemplateResponse("/play_videos/wanda_vision.html", {"request": request})

@router.get("/play_videos/insidius")
def getDados(request: Request):
        return templates.TemplateResponse("/play_videos/insidius.html", {"request": request})

@router.get("/play_videos/noite_bruxas")
def getDados(request: Request):
        return templates.TemplateResponse("/play_videos/noite_bruxas.html", {"request": request})

@router.get("/play_videos/exorcismo_papa")
def getDados(request: Request):
        return templates.TemplateResponse("/play_videos/exorcismo_papa.html", {"request": request})

@router.get("/play_videos/morte_demonio")
def getDados(request: Request):
        return templates.TemplateResponse("/play_videos/morte_demonio.html", {"request": request})

@router.get("/play_videos/transformes")
def getDados(request: Request):
        return templates.TemplateResponse("/play_videos/transformes.html", {"request": request})
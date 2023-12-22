from io import BytesIO
from fastapi import APIRouter, File, Form, Path, Request, UploadFile, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from models.Produto import Produto
from PIL import Image

from repositories.ProdutoRepo import ProdutoRepo

router = APIRouter(prefix="/produto")
templates = Jinja2Templates(directory="templates")

@router.get("/")
def getProdutos(request: Request):
    produtos = ProdutoRepo.obter_todos()
    return templates.TemplateResponse("produtos.html", {"request": request, "produtos": produtos})

@router.get("/inserir")
def getInserir(request: Request):
    return templates.TemplateResponse("inserir.html", {"request": request})

@router.post("/inserir")
async def postInserir(request: Request, nome: str = Form(), arquivoImagem: UploadFile = File()):    
    produto = Produto(nome=nome)
    ProdutoRepo.inserir(produto)
    conteudo_arquivo = await arquivoImagem.read()
    imagem = Image.open(BytesIO(conteudo_arquivo))
    imagem.save(f"static/img/produtos/{produto.id:04d}.jpg", "JPEG")
    return RedirectResponse("/produto", status.HTTP_302_FOUND)

@router.get("/excluir/{id:int}")
def getExcluir(request: Request, id: int = Path()):
    produto = ProdutoRepo.obter_um(id)
    return templates.TemplateResponse("excluir.html", {"request": request, "produto": produto})

@router.post("/excluir/{id:int}")
def postExcluir(request: Request, id: int = Path()):
    ProdutoRepo.excluir(id)
    return RedirectResponse("/produto", status.HTTP_302_FOUND)

@router.get("/alterar/{id:int}")
def getAlterar(request: Request, id: int = Path()):
    produto = ProdutoRepo.obter_um(id)
    return templates.TemplateResponse("alterar.html", {"request": request, "produto": produto})

@router.post("/alterar/{id:int}")
def postAlterar(
    request: Request, 
    id: int = Path(), 
    nome: str = Form()):
    ProdutoRepo.alterar(Produto(id, nome))
    return RedirectResponse("/produto", status.HTTP_302_FOUND)
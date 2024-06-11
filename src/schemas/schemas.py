from pydantic import BaseModel
from typing import Optional, List

class Usuario(BaseModel):
    id : Optional[str] = None
    nome : str
    telefone : str
    meus_produtos : List[Produto] # type: ignore
    minhas_vendas : List[Pedido] # type: ignore
    meus_pedidos : List[Pedido] # type: ignore

class Produto(BaseModel):
    id : Optional[str] = None
    usuario : Usuario
    nome : str
    detalhes : str
    preco : float
    disponivel : bool = False

class Pedido(BaseModel):
    id : Optional[str] = None
    usuario : Usuario
    produto : Produto
    quantidade : int
    entrega : bool = False
    endereco : str
    obs : Optional[str] = None

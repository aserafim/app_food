from pydantic import BaseModel
from typing import Optional, List


class Usuario(BaseModel):
    id : Optional[str] = None
    nome : str
    telefone : str
    meus_produtos : List[Produto]
    minhas_vendas : List[Pedido]
    meus_pedidos : List[Pedido]



class Produtos(BaseModel):
    id : Optional[str] = None
    usuario : Usuario
    nome : str
    detalhes : str
    preco : float
    disponivel : bool = False

class Pedido(BaseModel):
    id : Optional[str] = None
    usuario : Usuario
    produto : Produtos
    quantidade : int
    entrega : bool = False
    endereco : str
    obs : Optional[str] = None

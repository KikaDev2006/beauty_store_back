from typing import Optional
from decimal import Decimal
from ninja import Schema


class ProductoCreate(Schema):
    nombre: str
    descripcion: Optional[str] = None
    precio: Decimal
    estado: bool = True
    id_categoria: int
    imagen: Optional[str] = None


class ProductoUpdate(Schema):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[Decimal] = None
    estado: Optional[bool] = None
    id_categoria: Optional[int] = None
    imagen: Optional[str] = None


class ProductoOut(Schema):
    id: int
    nombre: str
    descripcion: Optional[str] = None
    precio: Decimal
    estado: bool
    id_categoria: int
    imagen: Optional[str] = None

    class Config:
        orm_mode = True

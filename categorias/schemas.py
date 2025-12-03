from typing import Optional
from ninja import Schema


class CategoriaCreate(Schema):
	nombre: str
	descripcion: Optional[str] = None


class CategoriaUpdate(Schema):
	nombre: Optional[str] = None
	descripcion: Optional[str] = None


class CategoriaOut(Schema):
	id: int
	nombre: str
	descripcion: Optional[str] = None

	class Config:
		orm_mode = True


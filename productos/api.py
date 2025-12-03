from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router

from .models import Producto
from .schemas import ProductoCreate, ProductoOut, ProductoUpdate

api = Router()


@api.get("", response=List[ProductoOut])
def list_productos(request):
	productos = Producto.objects.all()
	result = []
	for p in productos:
		result.append({
			"id": p.id,
			"nombre": p.nombre,
			"descripcion": p.descripcion,
			"precio": p.precio,
			"estado": p.estado,
			"id_categoria": p.id_categoria_id,
			"imagen": p.imagen.url if p.imagen else None,
		})
	return result


@api.get("/{producto_id}", response=ProductoOut)
def get_producto(request, producto_id: int):
	p = get_object_or_404(Producto, id=producto_id)
	return {
		"id": p.id,
		"nombre": p.nombre,
		"descripcion": p.descripcion,
		"precio": p.precio,
		"estado": p.estado,
		"id_categoria": p.id_categoria_id,
		"imagen": p.imagen.url if p.imagen else None,
	}


@api.post("", response=ProductoOut)
def create_producto(request, payload: ProductoCreate):
	data = payload.dict()
	categoria_id = data.pop("id_categoria")
	imagen = data.pop("imagen", None)
	producto = Producto.objects.create(id_categoria_id=categoria_id, **data)
	# nota: si quieres manejar subida de archivos, hay que aceptar UploadedFile
	return {
		"id": producto.id,
		"nombre": producto.nombre,
		"descripcion": producto.descripcion,
		"precio": producto.precio,
		"estado": producto.estado,
		"id_categoria": producto.id_categoria_id,
		"imagen": producto.imagen.url if producto.imagen else None,
	}


@api.put("/{producto_id}", response=ProductoOut)
def update_producto(request, producto_id: int, payload: ProductoUpdate):
	data = payload.dict(exclude_unset=True)
	if "id_categoria" in data:
		data["id_categoria_id"] = data.pop("id_categoria")
	Producto.objects.filter(id=producto_id).update(**data)
	p = get_object_or_404(Producto, id=producto_id)
	return {
		"id": p.id,
		"nombre": p.nombre,
		"descripcion": p.descripcion,
		"precio": p.precio,
		"estado": p.estado,
		"id_categoria": p.id_categoria_id,
		"imagen": p.imagen.url if p.imagen else None,
	}


@api.delete("/{producto_id}")
def delete_producto(request, producto_id: int):
	p = get_object_or_404(Producto, id=producto_id)
	p.delete()
	return {"ok": True}


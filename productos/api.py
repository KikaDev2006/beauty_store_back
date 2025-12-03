from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router

from .models import Producto
from .schemas import ProductoCreate, ProductoOut, ProductoUpdate

router = Router()


@router.get("", response=List[ProductoOut])
def list_productos(request):
    """List all productos"""
    return Producto.objects.all()


@router.get("/{producto_id}", response=ProductoOut)
def get_producto(request, producto_id: int):
    """Retrieve a single producto by id"""
    return get_object_or_404(Producto, id=producto_id)


@router.post("", response=ProductoOut)
def create_producto(request, payload: ProductoCreate):
    """Create a new producto"""
    data = payload.dict()
    categoria_id = data.pop("id_categoria")
    producto = Producto.objects.create(id_categoria_id=categoria_id, **data)
    return producto


@router.put("/{producto_id}", response=ProductoOut)
def update_producto(request, producto_id: int, payload: ProductoUpdate):
    """Update a producto fully or partially"""
    data = payload.dict(exclude_unset=True)
    if "id_categoria" in data:
        data["id_categoria_id"] = data.pop("id_categoria")
    Producto.objects.filter(id=producto_id).update(**data)
    return get_object_or_404(Producto, id=producto_id)


@router.delete("/{producto_id}")
def delete_producto(request, producto_id: int):
    """Delete a producto"""
    p = get_object_or_404(Producto, id=producto_id)
    p.delete()
    return {"ok": True}


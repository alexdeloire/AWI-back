from fastapi import APIRouter, Depends, Security
from typing import Annotated
from .auth import verify_token
from app.controllers.item_controller import (
    create_item,
    find_all_items,
    find_item_by_id,
    delete_item,
    delete_all_items,
)
from ..models.item import Item


item_router = APIRouter(
    prefix="/item",
    tags=["item"],
)
# Note it is possible to put dependencies on the router itself
# eg: dependencies=[Security(verify_token, scopes=["Admin"])]


@item_router.post("/", response_model=Item)
async def create_item_route(item: Item, token: Annotated[None, Security(verify_token, scopes=["Admin"])]):
    return await create_item(item)

@item_router.get("/", response_model=list[Item])
async def get_all_items_route(token: Annotated[None, Security(verify_token, scopes=["Admin"])]):
    return await find_all_items()

@item_router.get("/{id}", response_model=Item)
async def get_item_route(id: int, token: Annotated[None, Security(verify_token, scopes=["Admin"])]):
    return await find_item_by_id(id)

@item_router.delete("/{id}", response_model=dict)
async def delete_item_route(id: int, token: Annotated[None, Security(verify_token, scopes=["Admin"])]):
    return await delete_item(id)

@item_router.delete("/", response_model=dict)
async def delete_all_items_route(token: Annotated[None, Security(verify_token, scopes=["Admin"])]):
    return await delete_all_items()
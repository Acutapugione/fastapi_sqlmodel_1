"""Pizza routes"""

from typing import Any
from asyncio import sleep
from sqlmodel import select
from .db import DBConfig, Product
from . import app
from fastapi.requests import Request
from sqlmodel import Field, SQLModel, Enum

import enum


class Operators(enum.Enum):
    plus = "+"
    minus = "-"
    multy = "*"
    divide = "/"


async def get_data(__type: type, limit: int = -1, item_id: Any = None):
    """Return data from db"""
    await sleep(0.001)
    query_ = None
    if item_id:
        query_ = select(__type).where(__type.item_id == item_id).limit(1)
        return DBConfig.SESSION.scalar(query_)
    elif limit >= 0:
        query_ = select(__type).limit(limit)
    else:
        query_ = select(__type)

    return DBConfig.SESSION.scalars(query_)


@app.get("/pizza/list", response_model=list[Product])  # Dependency injection
async def pizza_list(
    # req: Request,
    limit: int = -1,
):
    """Return pizzas list"""
    return await get_data(Product, limit)


@app.get("/pizza/{item_id}", response_model=Product)  # Dependency injection
async def pizza_item(item_id: Any):
    """Return pizzas list"""
    return await get_data(Product, item_id=item_id)


class MathOperation(SQLModel, table=False):
    left_operand: float | int | str
    operator: Operators
    right_operand: float | int | str


@app.post("/multiply")
def multiply(operation: MathOperation):
    return {"result": operation.left_operand + operation.right_operand}

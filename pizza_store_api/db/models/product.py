from typing import Optional
from sqlmodel import Field
from .helpers import AutoIdIncrement


class Product(AutoIdIncrement, table=True):
    name: str
    description: Optional[str] = Field(default="", nullable=True)
    price: float

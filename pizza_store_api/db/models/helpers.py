from typing import Optional
from sqlmodel import Field, SQLModel


class AutoIdIncrement(SQLModel, table=False):
    item_id: Optional[int] = Field(default=None, primary_key=True)

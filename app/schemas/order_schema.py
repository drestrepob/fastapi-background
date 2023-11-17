from pydantic import BaseModel


class OrderSchema(BaseModel):
    dish: str

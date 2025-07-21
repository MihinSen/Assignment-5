from pydantic import BaseModel

class SandwichBase(BaseModel):
    name: str
    description: str
    price: float

class SandwichCreate(SandwichBase):
    pass

class SandwichUpdate(SandwichBase):
    pass

class Sandwich(SandwichBase):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel

# Order
class OrderBase(BaseModel):
    customer_name: str
    description: str

class OrderCreate(OrderBase): pass
class OrderUpdate(OrderBase): pass
class Order(OrderBase):
    id: int
    class Config:
        orm_mode = True

# Sandwich
class SandwichBase(BaseModel):
    name: str
    description: str
    price: float

class SandwichCreate(SandwichBase): pass
class SandwichUpdate(SandwichBase): pass
class Sandwich(SandwichBase):
    id: int
    class Config:
        orm_mode = True

# Resource
class ResourceBase(BaseModel):
    name: str
    quantity: int

class ResourceCreate(ResourceBase): pass
class ResourceUpdate(ResourceBase): pass
class Resource(ResourceBase):
    id: int
    class Config:
        orm_mode = True

# Recipe
class RecipeBase(BaseModel):
    sandwich_id: int
    resource_id: int
    quantity: int

class RecipeCreate(RecipeBase): pass
class RecipeUpdate(RecipeBase): pass
class Recipe(RecipeBase):
    id: int
    class Config:
        orm_mode = True

# Order Detail
class OrderDetailBase(BaseModel):
    order_id: int
    sandwich_id: int
    quantity: int

class OrderDetailCreate(OrderDetailBase): pass
class OrderDetailUpdate(OrderDetailBase): pass
class OrderDetail(OrderDetailBase):
    id: int
    class Config:
        orm_mode = True

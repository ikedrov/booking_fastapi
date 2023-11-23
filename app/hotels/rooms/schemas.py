from typing import Optional

from pydantic import BaseModel


class SRoom(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: str
    price: int
    services: Optional[list[str]]
    quantity: int
    image_id: int

    class Config:
        from_attributes = True


class SRoomsInfo(SRoom):
    total_cost: int
    rooms_left: int

    class Config:
        from_attributes = True
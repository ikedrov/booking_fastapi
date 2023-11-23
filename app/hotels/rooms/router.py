from datetime import date

from fastapi import APIRouter

from app.exceptions import (NoSuchHotelException, ToLongPeriodException,
                            WrongDateException)
from app.hotels.rooms.dao import RoomDAO
from app.hotels.rooms.schemas import SRoomsInfo

router = APIRouter(prefix='/rooms', tags=['Rooms'])


@router.get('/{hotel_id}/rooms')
async def get_rooms_by_date(hotel_id: int, date_from: date, date_to: date) -> list[SRoomsInfo]:
    if date_from > date_to:
        raise WrongDateException
    if (date_to - date_from).days > 31:
        raise ToLongPeriodException
    room = await RoomDAO.find_by_id(hotel_id)
    if not room:
        raise NoSuchHotelException
    rooms = await RoomDAO.find_all(hotel_id, date_from, date_to)

    return rooms

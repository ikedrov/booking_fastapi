
from datetime import date

from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.exceptions import (NoSuchHotelException, ToLongPeriodException,
                            WrongDateException)
from app.hotels.dao import HotelDAO
from app.hotels.schemas import SHotelInfo

router = APIRouter(prefix='/hotels', tags=['Hotels'])


@router.get('/{location}')
# @cache(expire=20)
async def get_hotels_by_location_and_date(location: str, date_from: date, date_to: date) -> list[SHotelInfo]:
    if date_from > date_to:
        raise WrongDateException
    if (date_to - date_from).days > 31:
        raise ToLongPeriodException
    hotels = await HotelDAO.find_all(location, date_from, date_to)
    if not hotels:
        raise NoSuchHotelException
    return hotels


@router.get('/id/{hotel_id}')
async def get_hotel_by_id(hotel_id: int):
    return await HotelDAO.find_one_or_none(id=hotel_id)

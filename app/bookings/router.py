from datetime import date

from fastapi import APIRouter, Depends
from pydantic import TypeAdapter

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking, SBookingInfo
from app.exceptions import NoSuchBookingException, RoomCannotBeBookedException
from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(prefix='/bookings', tags=['Bookings'])


@router.get('', status_code=200)
async def get_bookings(current_user: Users = Depends(get_current_user)) -> list[SBookingInfo]:
    booking = await BookingDAO.find_booking_for_user(user_id=current_user.id)
    if not booking:
        raise NoSuchBookingException
    return booking


@router.post('')
async def add_booking(room_id: int, date_from: date, date_to: date, user: Users = Depends(get_current_user)):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBookedException
    booking = TypeAdapter(SBooking).validate_python(booking).model_dump()
    # send_booking_confirmation_email.delay(booking, user.email)
    return booking


@router.delete('/{booking_id}', status_code=204)
async def delete_booking(booking_id: int, current_user: Users = Depends(get_current_user)):
    await BookingDAO.delete(id=booking_id, user_id=current_user.id)




from datetime import datetime

import pytest

from app.bookings.dao import BookingDAO


class TestBookingCRUD:

    @pytest.mark.parametrize('user_id, room_id,', [
        (2, 2),
        (2, 3),
        (1, 4),
        (1, 4),
        (-1, -1),
        ('w', 'w'),
        ('', '')
    ])
    async def test_add_and_get_booking(self, user_id, room_id):
        new_booking = await BookingDAO.add(
            user_id=user_id,
            room_id=room_id,
            date_from=datetime.strptime('2023-07-10', '%Y-%m-%d'),
            date_to=datetime.strptime('2023-07-24', '%Y-%m-%d')
        )
        if new_booking:
            assert new_booking.user_id == user_id
            assert new_booking.room_id == room_id
            booking = await BookingDAO.find_by_id(new_booking.id)
            assert booking is not None
        else:
            assert not new_booking

    async def test_add_and_delete_booking(self):
        new_booking = await BookingDAO.add(
            user_id=2,
            room_id=2,
            date_from=datetime.strptime('2023-07-10', '%Y-%m-%d'),
            date_to=datetime.strptime('2023-07-24', '%Y-%m-%d')
        )
        await BookingDAO.delete(id=new_booking.id)
        deleted_booking = await BookingDAO.find_one_or_none(id=new_booking.id)
        assert deleted_booking is None







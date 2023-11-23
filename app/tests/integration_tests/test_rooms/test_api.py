import pytest
from httpx import AsyncClient


@pytest.mark.parametrize('hotel_id, date_from, date_to, status_code, detail', [
    (1, '2023-11-13', '2023-11-12', 409, 'Date from can not be after date to'),
    (1, '2023-11-13', '2023-12-15', 409, 'Booking period must be less then 30 days'),
    ('qwerty', '2023-11-13', '2023-11-14', 422, None),
    (1, 'qwerty', 5, 422, None),
    ('', '', '', 404, 'Not Found'),
    (-1, '2023-11-13', '2023-11-14', 404, 'No such hotel'),
    (50, '2023-11-13', '2023-11-14', 404, 'No such hotel'),
    (1, '2023-11-13', '2023-11-14', 200, None)
])
async def test_get_rooms_by_date(hotel_id, date_from, date_to,
                                 status_code, detail, ac: AsyncClient):
    response = await ac.get(f'/rooms/{hotel_id}/rooms', params={
        'date_from': date_from,
        'date_to': date_to
    })
    assert response.status_code == status_code

    if str(status_code).startswith('4') and str(status_code) != '422':
        assert response.json()['detail'] == detail

import pytest
from httpx import AsyncClient


@pytest.mark.parametrize('location, date_from, date_to, status_code, detail', [
    ('Алтай', '2023-11-13', '2023-11-12', 409, 'Date from can not be after date to'),
    ('Алтай', '2023-11-13', '2023-12-15', 409, 'Booking period must be less then 30 days'),
    ('qwerty', '2023-11-13', '2023-11-14', 404, 'No such hotel'),
    ('Алтай', 'qwerty', 5, 422, None),
    ('', '', '', 404, 'Not Found'),
    ('Алтай', '2023-11-13', '2023-11-14', 200, None)

])
async def test_get_hotels_by_location_and_date(location, date_from, date_to,
                                               status_code, detail, ac: AsyncClient):
    response = await ac.get(f'/hotels/{location}', params={
        'date_from': date_from,
        'date_to': date_to
    })
    assert response.status_code == status_code
    if str(status_code).startswith('4') and str(status_code) != '422':
        assert response.json()['detail'] == detail


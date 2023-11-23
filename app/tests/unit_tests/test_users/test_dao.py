import pytest

from app.users.dao import UsersDAO


@pytest.mark.parametrize('user_id, email, exists', [
    (1, 'test@test.com', True),
    (2, 'artem@example.com', True),
    (3, 'qwerty@qw.com', False)
])
async def test_find_user_by_id(user_id, email, exists):
    user = await UsersDAO.find_by_id(user_id)
    if exists:
        assert user
        assert user.id == user_id
        assert user.email == email
    else:
        assert not user


@pytest.mark.parametrize('email, exists', [
    ('test@test.com', True),
    ('artem@example.com', True),
    ('qwerty@qw.com', False)
])
async def test_find_user_by_email(email, exists):
    user = await UsersDAO.find_one_or_none(email=email)
    if exists:
        assert user
        assert user['email'] == email
    else:
        assert not user





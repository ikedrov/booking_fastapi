from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'User already exists'


class IncorrectEmailOrPasswordException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Incorrect Email or Password'


class TokenExpiredException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Token has been expired'


class NoTokenException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'No token'


class IncorrectFormatTokenException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Incorrect token format'


class NoUserException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED


class RoomCannotBeBookedException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'No rooms left'


class NoSuchBookingException(BookingException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No such booking'


class NoSuchHotelException(BookingException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No such hotel'


class WrongDateException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Date from can not be after date to'


class ToLongPeriodException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Booking period must be less then 30 days'


class CanNotUploadException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Can not upload file'





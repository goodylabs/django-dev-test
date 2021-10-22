"""
Module containing validators definitions.
"""
from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.timezone import (
    localtime,
    now,
)


@deconstructible
class LessThanNowValidator:
    """
    Validator checking that the date is not later than current date and time
    """
    message = 'The date cannot be later current date and time.'
    code = 'future_error'

    def __init__(self, message: str = None, code: str = None):
        """
        The constructor of the class LessThanNowValidator.

        :param message: error message
        :param code: error code
        """

        if message:
            self.message = message

        if code:
            self.code = code

    def __eq__(self, other: object):
        return (
                isinstance(other, self.__class__) and
                self.code == other.code and
                self.message == other.message
        )

    def __call__(self, i_date: datetime):
        if i_date > localtime(now()):
            raise ValidationError(self.message, self.code)

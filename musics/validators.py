from django.core.exceptions import ValidationError
from stdnum.util import clean, isdigits

# name = models.CharField(max_length=50) #TODO Validators
#     band = models.CharField(max_length=50) #TODO Validators
#     record_company = models.CharField(max_length=50) #TODO Validators
#     category = models.CharField(max_length=25) #TODO Validators
#     universal_code = models.CharField(max_length=13) #TODO Validators
#     published_by = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now = True)
import re


# TODO Refactoring dei validators, pensare a delle possibili validazioni aggiuntive per i campi.
def validate_name(value: str) -> None:
    if len(value) == 0:
        raise ValidationError('Name must not be empty')
    if not re.match('[A-Za-z0-9- ,!@]', value):
        raise ValidationError(
            "Name format can contain only letters,numbers and special characters as '-', ',' and whitespaces")


def validate_artist(value: str) -> None:
    if len(value) == 0:
        raise ValidationError('Artist name must not be empty')
    if not re.match('[A-Za-z0-9- ,!@]', value):
        raise ValidationError(
            "Artist name format can contain only letters,numbers and special characters as '-', ',' and whitespaces")


def validate_record_company(value: str) -> None:
    if len(value) == 0:
        raise ValidationError('Record company name must not be empty')
    if not re.match('[A-Za-z0-9- ,!@#]', value):
        raise ValidationError(
            "Record company name format can contain only letters,numbers and special characters as '-', ',' and whitespaces")


def validate_genre(value: str) -> None:
    if len(value) == 0:
        raise ValidationError('Genre name must not be empty')
    if not value[0].isupper():
        raise ValidationError('Genre must be capitalized')
    if not re.match('^[A-Z][A-Za-z ]', value):
        raise ValidationError("Genre name format can contain only letters and whitespaces")


def ean_calc_check_digit(number):
    """Calculate the EAN check digit for 13-digit numbers. The number passed
    should not have the check bit included."""
    return str((10 - sum((3, 1)[i % 2] * int(n)
                         for i, n in enumerate(reversed(number)))) % 10)


def validate_ean(number):
    """Check if the number provided is a valid EAN-13. This checks the length
    and the check bit but does not check whether a known GS1 Prefix and
    company identifier are referenced."""
    number = clean(number, ' -').strip()
    if not isdigits(number):
        raise ValidationError("EANCode is structured with numbers.")
    if len(number) not in (14, 13, 12, 8):
        raise ValidationError("EANCode length isn't correct.")
    if ean_calc_check_digit(number[:-1]) != number[-1]:
        raise ValidationError("Checksum fails.")
    return number


def ean_is_valid(number):
    """Check if the number provided is a valid EAN-13. This checks the length
    and the check bit but does not check whether a known GS1 Prefix and
    company identifier are referenced."""
    try:
        return bool(validate_ean(number))
    except ValidationError:
        return False

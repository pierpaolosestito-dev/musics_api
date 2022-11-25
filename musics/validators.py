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
#TODO Refactoring dei validators, pensare a delle possibili validazioni aggiuntive per i campi.
def validate_name(value:str) -> None:
    if len(value) == 0:
        raise ValidationError('Name must not be empty')
    if not re.match('[A-Za-z0-9- ,]',value):
        raise ValidationError("Name format can contain only letters,numbers and special characters as '-', ',' and whitespaces")

def validate_band(value:str)->None:
    if len(value) == 0:
        raise ValidationError('Band name must not be empty')
    if not re.match('[A-Za-z0-9- ,]',value):
        raise ValidationError("Band name format can contain only letters,numbers and special characters as '-', ',' and whitespaces")

def validate_record_company(value:str)->None:
    if len(value) == 0:
        raise ValidationError('Record company name must not be empty')
    if not re.match('[A-Za-z0-9- ,]',value):
        raise ValidationError("Record company name format can contain only letters,numbers and special characters as '-', ',' and whitespaces")

def validate_category(value:str)->None:
    if len(value) == 0:
        raise ValidationError('Category name must not be empty')
    if not re.match('[A-Za-z0-9- ,]',value):
        raise ValidationError("Category name format can contain only letters,numbers and special characters as '-', ',' and whitespaces")

def validate_ean_code(value:str)->None: #TODO Sicuro da migliorare
    if len(value) != 13:
        raise ValidationError("EAN-13 Code must be 13 characters long")
    if not re.match('^[0-9]{13}$',value):
        raise ValidationError("EAN-13 Code format isn't correct")


class EANCodeValidator:
    def compact(self,number):
        """Convert the EAN to the minimal representation. This strips the number
        of any valid separators and removes surrounding whitespace."""
        return clean(number, ' -').strip()

    def calc_check_digit(self,number):
        """Calculate the EAN check digit for 13-digit numbers. The number passed
        should not have the check bit included."""
        return str((10 - sum((3, 1)[i % 2] * int(n)
                             for i, n in enumerate(reversed(number)))) % 10)

    def validate(self,number):
        """Check if the number provided is a valid EAN-13. This checks the length
        and the check bit but does not check whether a known GS1 Prefix and
        company identifier are referenced."""
        number = self.compact(number)
        if not isdigits(number):
            raise ValidationError("EANCode is structured with numbers.")
        if len(number) not in (14, 13, 12, 8):
            raise ValidationError("EANCode length isn't correct.")
        if self.calc_check_digit(number[:-1]) != number[-1]:
            raise ValidationError("Checksum fails.")
        return number

    def is_valid(self,number):
        """Check if the number provided is a valid EAN-13. This checks the length
        and the check bit but does not check whether a known GS1 Prefix and
        company identifier are referenced."""
        try:
            return bool(self.validate(number))
        except ValidationError:
            return False


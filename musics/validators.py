from django.core.exceptions import ValidationError

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

def validate_ean_code_13(value:str)->None:
    if len(value) != 13:
        raise ValidationError("EAN-13 Code must be 13 characters long")
    if not re.match('^[0-9]{13}$',value):
        raise ValidationError("EAN-13 Code format isn't correct")


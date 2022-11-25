from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from django.db import models
from musics.validators import validate_name, validate_band, validate_record_company, validate_category, \
    validate_ean_code


#CD:#
#- Nome ->
#- Band/Artista
#- Casa discografica
# - Categoria
# - Codice(UPC/EAN)
# - Prezzo
# - Pubblicato_da
# Create your models here.
class CD(models.Model):
    name = models.CharField(max_length=50,validators=[validate_name])
    artist = models.CharField(max_length=50,validators=[validate_band])
    record_company = models.CharField(max_length=50,validators=[validate_record_company])
    genre = models.CharField(max_length=25,validators=[validate_category])
    ean_code = models.CharField(max_length=13, validators=[validate_ean_code]) #TODO Validators: Refactoring ean_code_13 validator
    published_by = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.band + " " + self.name


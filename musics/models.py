from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from django.db import models


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
    name = models.CharField(max_length=50) #TODO Validators
    band = models.CharField(max_length=50) #TODO Validators
    record_company = models.CharField(max_length=50) #TODO Validators
    category = models.CharField(max_length=25)
    universal_code = models.CharField(max_length=13)
    published_by = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)



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




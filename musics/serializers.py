from djmoney.money import Money
from rest_framework import serializers

from musics.models import CD

class CDSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'artist', 'record_company', 'genre','ean_code','price','price_currency','published_by','created_at','updated_at')
        model = CD


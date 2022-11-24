from rest_framework import serializers

from musics.models import CD

class CDSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'band', 'record_company', 'category','ean_code_13','published_by','created_at','updated_at')
        model = CD
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import Group
from rest_framework import serializers


from musics.models import CD

class CDSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'artist', 'record_company', 'genre','ean_code','price','price_currency','published_by','created_at','updated_at')
        model = CD


list_allowed_group = ['publishers']
class RegistrationSerializer(RegisterSerializer):
    group = serializers.CharField(required=False)

    def custom_signup(self, request, user):
        _group = self.validated_data.get('group','')
        if _group in list_allowed_group:
            group_getted_by_django = Group.objects.get(name=_group)
            group_getted_by_django.user_set.add(user)
        else:
            raise serializers.ValidationError("Group isn't allowed") #TODO Fabrizio

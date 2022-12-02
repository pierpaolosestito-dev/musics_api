from dj_rest_auth.models import TokenModel
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import Group, User
from rest_framework import serializers


from musics.models import CD

class CDSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="published_by.username",read_only=True)
    class Meta:
        fields = ('id', 'name', 'artist', 'record_company', 'genre','ean_code','price','price_currency','published_by','user','created_at','updated_at')
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id','username'
        )
class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False,read_only=True)
    class Meta:
        model = TokenModel
        fields = ('key','user')
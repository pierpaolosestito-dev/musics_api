from dj_rest_auth.models import TokenModel
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import Group, User
from djmoney.contrib.django_rest_framework import MoneyField
from rest_framework import serializers


from musics.models import CD

class CDSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="published_by.username",read_only=True)
    price = MoneyField(max_digits=8,decimal_places=2)
    class Meta:
        fields = ('id', 'name', 'artist', 'record_company', 'genre', 'ean_code',
                  'price', 'price_currency', 'published_by', 'user', 'created_at', 'updated_at')
        model = CD


list_allowed_group = ['publishers']
class RegistrationSerializer(RegisterSerializer):
    group = serializers.CharField(required=False)

    def validate(self, data):
        if 'group' in data and data['group'] not in list_allowed_group:
            raise serializers.ValidationError({"group": "Group isn't allowed"})
        return super().validate(data)

    def custom_signup(self, request, user):
        validated_group = self.validated_data.get('group', '')
        if validated_group:
            group = Group.objects.get(name=validated_group)
            group.user_set.add(user)


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
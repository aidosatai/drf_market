from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate

from account.models import CustomUser

class CustomUserAllFieldsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = 'first_name', 'last_name', 'phone', 'email', 'iin'


class CustomUserListSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(format='%d-%m-%y %H:%M')

    class Meta:
        model = CustomUser
        fields = 'uuid', 'first_name', 'last_name', \
                 'phone', 'email', 'iin', 'last_login', 'is_active', 'role'


class CustomUserLoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, required=True)

    class Meta:
        fields = 'phone', 'password'

    def validate(self, attrs):
        phone = attrs.get('phone') or None

        try:
            user = CustomUser.objects.get(phone=phone)
            attrs['user'] = user
        except ObjectDoesNotExist as e:
            print(e)
            raise ValidationError('ERROR: By given phone number user not exist!')

        return attrs

    def login_user(self):
        try:
            request = self.context.get('request')
            login(request, self.validated_data.get('user'))
            return True
        except Exception as ex:
            print(ex)
            raise ValidationError('ERROR: Something wrong login, try again later!')
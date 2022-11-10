import random

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate

from rest_framework_simplejwt.authentication import authentication

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
                 'phone', 'email', 'iin', 'last_login', 'is_active', 'role', 'is_staff'


class CustomUserLoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, required=False)

    class Meta:
        fields = 'phone', 'password'

    def validate(self, attrs):
        phone = attrs.get('phone') or None
        password = attrs.get('password') or None

        try:
            user = CustomUser.objects.get(phone=phone)
            attrs['user'] = user
            if user.check_password(password):
                attrs['otp'] = False
            else:
                attrs['otp'] = random.randrange(1000, 9999)
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


class CheckUserOTPSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=100, required=True)
    otp = serializers.IntegerField(max_value=9999, min_value=1000, required=True)

    class Meta:
        fields = 'phone', 'otp'


    def validate(self, attrs):
        from django.core.cache import cache
        phone = attrs.get('phone') or None
        otp = attrs.get('otp') or None
        user = CustomUser.objects.filter(phone__exact=phone).first()

        if user is None:
            raise ValidationError('ERROR: By given phone number user not exist!')

        old_otp = cache.get(user.email)
        if old_otp is None:
            raise ValidationError('Old OTP not found! Please, resend!')

        if old_otp.get('otp') != otp:
            raise ValidationError('ERROR: OTP incorrect')
        else:
            cache.delete(user.email)
            attrs['user'] = user

        return attrs

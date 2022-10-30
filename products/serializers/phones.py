from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from products.models import Phone, Memory
from utils.const import PhoneCompanyChoice, PhoneColorChoice

class PhoneAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        fields = '__all__'


class PhoneListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d-%m-%y %H-%M')
    updated_at = serializers.DateTimeField(format='%d-%m-%y %H-%M')
    memory = serializers.SerializerMethodField('get_memory')

    class Meta:
        model = Phone
        fields = 'uuid', 'company', 'model', 'color', 'price', 'created_at', 'updated_at', 'memory'

    def get_memory(self, instance):
        if instance.memory is not None:
            return instance.memory.size

class PhoneRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        fields = 'company', 'model', 'color', 'price', 'memory'


class PhoneCreateSerializer(serializers.ModelSerializer):
    company = serializers.CharField(max_length=255, required=False, allow_blank=True),
    memory = serializers.IntegerField(default=0, required=False, allow_null=True)

    class Meta:
        model = Phone
        fields = 'company', 'model', 'color', 'price', 'memory'

    def validate(self, attrs):
        memory = attrs.get('memory') or None
        company = attrs.get('company') or None
        color = attrs.get('color') or None

        if color is None:
            raise ValidationError('ERROR: Color data not found!')
        elif color not in PhoneColorChoice.values:
            raise  ValidationError('ERRPR: Given color value is not correct')
        if company is None:
            raise ValidationError('ERROR: Company data not found')
        if memory is None:
            raise ValidationError('ERROR: Memory data not found')

        if company == PhoneCompanyChoice.APPLE.value and memory == 64:
            raise ValidationError('EXCEPTION: Apple Phones not have option to 64Gb memory size')
        elif company not in PhoneCompanyChoice.values:
            raise ValidationError('EXCEPTION: Given Company value is not correct')
        else:
            attrs['memory'], created = Memory.objects.get_or_create(size=int(memory))

        return attrs

    def create(self, validated_data):
        return super(PhoneCreateSerializer, self).create(validated_data)

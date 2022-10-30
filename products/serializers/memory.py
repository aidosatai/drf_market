from rest_framework import serializers

from products.models import Memory


class MemoryAllFieldsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Memory
        fields = '__all__'

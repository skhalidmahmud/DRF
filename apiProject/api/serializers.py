from rest_framework import serializers
from . import models

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.studentModel
        fields = '__all__'

    def create(self, validated_data):
        data = models.studentModel.objects.create(**validated_data)
        data.studentRoll = 50
        data.save()
        return data
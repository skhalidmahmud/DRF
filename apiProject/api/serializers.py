from rest_framework import serializers
from . import models

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.studentModel
        fields = '__all__'

    def create(self, validated_data):
        name = validated_data.get('Name')
        last_man = models.studentModel.objects.order_by('-studentRoll').first()
        last_roll = last_man.studentRoll
        if last_roll:
            last_roll = last_roll+1
        else:
            last_roll = 1
        data = models.studentModel.objects.create(**validated_data)
        data.username = name + str(last_roll)
        data.studentRoll = last_roll
        data.save()
        return data
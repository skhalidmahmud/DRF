from rest_framework import serializers
from . import models

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.studentModel
        fields = '__all__'
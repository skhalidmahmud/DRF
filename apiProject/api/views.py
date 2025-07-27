from django.shortcuts import render
from api.models import studentModel
from api.serializers import studentSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def studentData(req):
    if req.method == 'GET':
        data = studentModel.objects.all()
        serializer = studentSerializer(data, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
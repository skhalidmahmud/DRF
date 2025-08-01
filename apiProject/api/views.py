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

@api_view(['POST'])
def addStudent(req):
    serializer = studentSerializer(data = req.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'success': True,
            'mrssage': 'student data add successfully',
            'data': serializer.data
        })
    else:
        return Response({
            'success': False,
            'mrssage': 'Invlid Operation',
        })
    
@api_view(['PUT'])
def updateStudent(req, pk):
    student = studentModel.objects.get(id=pk)
    studentData = studentSerializer(student, data = req.data, partial = True) # 'partial' use for partial update
    if studentData.is_valid():
        studentData.save()
        return Response(studentData.data)
    else:
        return Response(studentData.errors)
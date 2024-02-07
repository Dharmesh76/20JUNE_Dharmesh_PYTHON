from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# Create your views here.
# to get all data in json api

@api_view(['GET'])
def getall(request):
    if request.method=='GET':
        book_data=BookModel.objects.all()
        serial=BookSerializers(book_data,many=True)
        return Response(serial.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# to get specific data in json api
@api_view(['GET'])
def getId(request,id):
    if request.method=='GET':
        try:
            book_data=BookModel.objects.get(id=id)
            serial=BookSerializers(book_data)
            return Response(serial.data,status=status.HTTP_302_FOUND)
        except BookModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE','GET'])
def delete_data(request,id):
    try:
        book_data=BookModel.objects.get(id=id)
    except BookModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=BookSerializers(book_data)
        return Response(serial.data,status=status.HTTP_200_OK)
    if request.method=='DELETE':
        BookModel.delete(book_data)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_data(request):
    if request.method=='POST':
        serial=BookSerializers(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
        

@api_view(['PUT','GET'])
def update_data(request,id):
    try:
        book_data=BookModel.objects.get(id=id)
    except BookModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=BookSerializers(book_data)
        return Response(serial.data,status=status.HTTP_302_FOUND)
    if request.method=='PUT':
        serial=BookSerializers(data=request.data,instance=book_data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)


    
      
from django.shortcuts import render

# Create your views here.

# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer

# class HelloView(APIView):
#     permission_classes = (IsAuthenticated,)             # <-- And here

#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def hello_view(request):
#     permission_classes = (IsAuthenticated,) 
#     content = {'message': 'Hello, World!'}
#     return Response(content)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def product_list(request):
    if request.method == 'GET':
        obj = Product.objects.all()
        serializer = ProductSerializer(obj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def product_details(request,pk):
    try:
        obj = Product.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializer(obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
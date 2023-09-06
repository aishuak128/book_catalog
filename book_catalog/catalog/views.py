from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer, BookListSerializer 


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class BookAPIView(APIView):
    def get(self, request, **kwargs):
        id = kwargs.get('id', None)

        if not id:
            return Response({'error': 'Method GET not allowed'})
        try:
            book = Book.objects.get(id=id)
        except:
            return Response({'error': "Object doesn't exist"})

        serializer = BookSerializer(book)

        return Response({'book': serializer.data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) 
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        if not id:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Book.objects.get(id=id)
        except:
            return Response({'error': "Object doesn't exist"})

        serializer = BookSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})
        

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer 


# class BookAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookAPIView(APIView):
    def get(self, request):
        qs = Book.objects.all()
        return Response({'books': BookSerializer(qs, many=True).data})

    def post(self, request):
        print(f'{request.data=}')
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) 
        post_new = Book.objects.create(**request.data)

        return Response({'post': BookSerializer(post_new).data})


 
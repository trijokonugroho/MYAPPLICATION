from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import BookSerializers
from . models import Book

class BookList(APIView):
    def get(self, request, Book_id=None):
        if Book_id is not None:
            try:
                book = Book.objects.get(id=Book_id)
                serializer = BookSerializers(book)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Book.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                books = Book.objects.all()
                serializers = BookSerializers(books, many=True)
                return Response(serializers.data, status=status.HTTP_200_OK)
            except Book.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request):
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, Book_id):
        try:
            book = Book.objects.get(id=Book_id)
            serializer = BookSerializers(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, Book_id):
        try:
            book = Book.objects.get(id=Book_id)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
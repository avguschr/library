from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView
from library.models import Book, Author
from library.serializers import BookSerializer, AuthorSerializer, CreateBookSerializer
from rest_framework.permissions import IsAdminUser


class BookView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_fields = (
        'title',
        'author',
        'genre',
    )


class AuthorView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CreateBookView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = CreateBookSerializer
    permission_classes = [IsAdminUser]

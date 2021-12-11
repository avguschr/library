from rest_framework import serializers

from library.models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = (
        #     'title',
        #     'author',
        #     'yearOfRel',
        #     'genre',
        #     'category',
        #     'publisher'
        # )


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'name',
            'lastName',
            'middle_name',
            'dateOfBirth'
        )


class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'title',
            'author',
            'yearOfRel',
            'genre',
            'category',
            'publisher'
        )

from django.contrib import admin

# Register your models here.
from library.models import User, Author, Cover, Book

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Cover)
admin.site.register(Book)
from django.urls import path
from library.views import AuthorView, BookView, CreateBookView, BookListView

app_name = 'library'

urlpatterns = [
    path('book/<int:pk>', BookView.as_view(), name='book'),
    path('book', BookListView.as_view(), name='books'),
    path('author/<int:pk>', AuthorView.as_view(), name='author'),
    path('createBook', CreateBookView.as_view(), name='create_book')
]

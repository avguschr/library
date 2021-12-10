from django.urls import path
from library.views import AuthorView, BookView, CreateBookView

app_name = 'library'

urlpatterns = [
    path('book/<int:pk>', BookView.as_view(), name='book'),
    path('author/<int:pk>', AuthorView.as_view(), name='author'),
    path('createBook', CreateBookView.as_view(), name='create_book')
]

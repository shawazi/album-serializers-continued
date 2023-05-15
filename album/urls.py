from django.urls import path
from .views import home, genre_view, album_view, genre_detail

urlpatterns = [
    path('', home),
    path('genre/', genre_view),
    path('genre/<int:pk>/', genre_detail),
    path('album/', album_view),
]   
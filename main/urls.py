"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from album.views import ArtistList, ArtistDetail, AlbumList, AlbumDetail, SongList, SongDetail, GenreList, GenreDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("album.urls")), 
    
    path('genre/', GenreList.as_view(), name='genre-list'),
    path('genre/<int:pk>/', GenreDetail.as_view(), name='genre-detail'),
    path('artists/', ArtistList.as_view(), name='artist-list'),
    path('artists/<int:pk>/', ArtistDetail.as_view(), name='artist-detail'),
    path('albums/', AlbumList.as_view(), name='album-list'),
    path('albums/<int:pk>/', AlbumDetail.as_view(), name='album-detail'),
    path('songs/', SongList.as_view(), name='song-list'),
    path('songs/<int:pk>/', SongDetail.as_view(), name='song-detail'),
]
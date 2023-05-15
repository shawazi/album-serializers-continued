from django.shortcuts import HttpResponse, get_object_or_404
from rest_framework import generics
from .models import Artist, Album, Song, Genre
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer, GenreSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET", "POST"])
def genre_view(request):
    
    if request.method == "POST":
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            # Genre.object.create(**serializer.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    all_genres = Genre.objects.all()
    serializer = GenreSerializer(all_genres, many=True)
    return Response(serializer.data)

@api_view(["GET", "POST"])
def album_view(request):
    
    if request.method == "POST":
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            # Album.object.create(**serializer.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    data = Album.objects.all()
    serializer = AlbumSerializer(data, many=True)
    return Response(serializer.data)

@api_view(["GET", "PUT", "PATCH", "DELETE"])
def genre_detail(request, pk):
    if request.method == "GET":
        # data = Genre.objects.get(pk=pk)
        data = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(data)
        return Response(serializer.data)
    elif request.method == "PUT":
        data = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "PUT":
        data = get_object_or_404(Genre, pk=pk)
        data.delete()
        return Response({"message" : "delete successful"})
        
def home(request):
    return HttpResponse("<h3>Welcome to Album API</h3>")

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

from rest_framework import serializers
from .models import Genre, Album, Song, Artist


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

class AlbumSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField() # not available for POST method
    genre_id = serializers.IntegerField(write_only=True) # not available for GET method
    # records = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    records = serializers.StringRelatedField(many=True, read_only=True) #read_only necessary to avoid API from demanding records for POST
    class Meta:
        model = Album
        fields = ('id', 'genre','genre_id', 'title', 'release_date', 'records')
        
class SongSerializer(serializers.ModelSerializer):
    album = serializers.StringRelatedField()
    album_id = serializers.IntegerField()
    class Meta:
        model = Song
        fields = ('id','album','album_id', 'title','track_number','length')

class ArtistSerializer(serializers.ModelSerializer):
    # albums = serializers.StringRelatedField(many=True)
    class Meta:
        model = Artist
        fields = ('id', 'albums', 'name')
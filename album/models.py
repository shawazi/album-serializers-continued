from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Album(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    title = models.CharField(max_length=50)
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="records")
    title = models.CharField(max_length=50)
    track_number = models.IntegerField()
    length = models.IntegerField()

    def __str__(self):
        return f"{self.album} - {self.title}"

class Artist(models.Model):
    albums = models.ManyToManyField(Album)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



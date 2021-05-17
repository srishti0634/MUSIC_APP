from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Album(models.Model):
    album_title= models.CharField(max_length=250)
    photo= models.CharField(max_length=200)

    def __str__(self):
        return self.album_title

class Movie(models.Model):
    movie_title= models.CharField(max_length=250)
    photo= models.CharField(max_length=200)

    def __str__(self):
        return self.movie_title

class Singer(models.Model):
    singer_title= models.CharField(max_length=250)
    photo= models.CharField(max_length=200)

    def __str__(self):
        return self.singer_title

class Songs(models.Model):
    song_title= models.CharField(max_length=200)
    photo= models.CharField(max_length=200)
    album= models.ForeignKey(Album, on_delete=models.CASCADE,blank=True)
    movie= models.ForeignKey(Movie, on_delete=models.CASCADE)
    singer= models.ForeignKey(Singer, on_delete=models.CASCADE)
    occassion=models.CharField(max_length=200,blank=True)
    mood=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    file_type= models.CharField(max_length=10)
    yr_of_rel=models.IntegerField()
    lyrics=models.TextField(blank=True)
    popularity=models.IntegerField()

    def __str__(self):
        return self.song_title +' - '+ self.singer.singer_title

class Playlist(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_title= models.CharField(max_length=200)
    add_to_playlist=models.ManyToManyField(Songs,blank=True)

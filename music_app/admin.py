from django.contrib import admin
from music_app.models import Album,Songs,Movie,Singer,Playlist

# Register your models here.
admin.site.register(Album)
admin.site.register(Songs)
admin.site.register(Movie)
admin.site.register(Singer)
admin.site.register(Playlist)

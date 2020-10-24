from django.conf.urls import url
from music_app import views

app_name='music_app'

urlpatterns=[
    url(r'^$', views.Homeview, name='home'),
    url(r'^register/',views.register,name='register'),
    url(r'^login/',views.loginpage,name='login'),
    url(r'^logout/',views.logoutpage,name='logout'),
    url(r'^latest_hindi/(?P<my_id>\d+)/', views.latest_hindi, name='latest_hindi'),
    url(r'^eng_song/(?P<my_id>\d+)/', views.eng_song, name='eng_song'),
    url(r'^punjabi_song/(?P<my_id>\d+)/', views.punjabi_song, name='punjabi_song'),
    url(r'^inter_song/(?P<my_id>\d+)/', views.inter_song, name='inter_song'),
    url(r'^romantic_song/(?P<my_id>\d+)/', views.romantic_song, name='romantic_song'),
    url(r'^sad_song/(?P<my_id>\d+)/', views.sad_song, name='sad_song'),
    url(r'^happy_song/(?P<my_id>\d+)/', views.happy_song, name='happy_song'),
    url(r'^playlist/',views.playlist,name='playlist'),
    # url(r'^create/',views.create,name='create'),
]

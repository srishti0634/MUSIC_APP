from django.shortcuts import render,redirect
from django.urls import reverse
# from music_app.models import Songs,Album
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from music_app.models import Album,Songs,Singer,Movie,Playlist

# Create your views here.

def Homeview(request):
    hindi_song = Songs.objects.filter(genre='Latest hindi')
    eng_song = Songs.objects.filter(genre='Latest english')
    punjabi_song = Songs.objects.filter(genre='Punjabi')
    inter_song = Songs.objects.filter(genre='International')
    romantic_song = Songs.objects.filter(mood='Romantic')
    sad_song = Songs.objects.filter(mood='Sad')
    happy_song = Songs.objects.filter(mood='Happy')
    return render(request,'home.html', {'hindi_song': hindi_song, 'eng_song':eng_song, 'punjabi_song':punjabi_song, 'inter_song':inter_song, 'romantic_song':romantic_song, 'sad_song':sad_song, 'happy_song':happy_song,})

def register(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            login(request,user)
            return HttpResponseRedirect(reverse('music_app:home'))
    return render(request,"register.html",{'form':form})

@login_required
def logoutpage(request):
    logout(request)
    return HttpResponseRedirect(reverse('music_app:home'))

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('music_app:home'))
        else:
            messages.error(request,'username or password not correct')
            return redirect('music_app:login')

    return render(request,"login.html",{})

def latest_hindi(request,my_id):
    check=Songs.objects.get(id=my_id)
    songplay = Songs.objects.filter(genre='Latest hindi')
    return render(request, "songplay.html", {'songplay': songplay,'check':check})

def eng_song(request,my_id):
    check=Songs.objects.get(id=my_id)
    songplay = Songs.objects.filter(genre='Latest english')
    return render(request, "songplay.html", {'songplay': songplay,'check':check})

def punjabi_song(request,my_id):
    check=Songs.objects.get(id=my_id)
    songplay = Songs.objects.filter(genre='Punjabi')
    return render(request, "songplay.html", {'songplay': songplay,'check':check})

def inter_song(request,my_id):
    check=Songs.objects.get(id=my_id)
    songplay = Songs.objects.filter(genre='International')
    return render(request, "songplay.html", {'songplay': songplay,'check':check})

def romantic_song(request,my_id):
    check=Songs.objects.get(id=my_id)
    songplay = Songs.objects.filter(mood='Romantic')
    return render(request, "songplay.html", {'songplay': songplay,'check':check})

def sad_song(request,my_id):
    check=Songs.objects.get(id=my_id)
    songplay = Songs.objects.filter(mood='Sad')
    return render(request, "songplay.html", {'songplay': songplay,'check':check})

def happy_song(request,my_id):
    check=Songs.objects.get(id=my_id)
    songplay = Songs.objects.filter(mood='Happy')
    return render(request, "songplay.html", {'songplay': songplay,'check':check})

def playlist(request):
    return render(request,"playlist.html",{})

# def newplaylist(request):
#     if request.method=='POST':
#         user=request.user
#         name=request.POST['playlist_name']
#         add_song_id=request.POST['playlist_song_id']
#         song=Songs.objects.get(id=add_song_id)
#         print(song)
#         # p=Playlist(user=user,playlist_title=name)
#         # p.add_to_playlist.add(song)
#         # p.save()
#         # return redirect(f"music_app/{Songs[add_song_id].genre}/{add_song_id}")
#     return HttpResponse("helllloooo")
#         # user=request.user
#         # name=request.POST['playlist_name']
#         # print(name)
#         # add_song_id=request.POST['playlist_song_id']
#         # song=Songs.objects.get(id=add_song_id)
#         #
#         # playlist=Playlist.objects.filter(user=user)
#         # return redirect(f"music_app/{Songs[add_song_id].genre}/{add_song_id}")

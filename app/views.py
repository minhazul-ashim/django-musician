from django.shortcuts import render, redirect;
from . import forms;
from . import models;

# Create your views here.
def addMusician(request) :
    addForm = forms.MusicianForm;
    if request.method == 'POST' :
        form =  forms.MusicianForm(request.POST)
        if(form.is_valid()) :
            form.save();
            return redirect('addMusicianPage');
    else :
        form = forms.MusicianForm();
    return render(request, 'addMusician.html', {"form" : addForm});

# Create your views here.
def listMusicians(request) :
    data = models.Musician.objects.all();
    return render(request, 'musicians.html', {"data" : data});

# Create your views here.
def editMusician(request) :
    return render(request, 'editMusician.html');

# Create your views here.
def addAlbum(request) :
    addForm = forms.AlbumForm;
    if request.method == 'POST' :
        form =  forms.AlbumForm(request.POST)
        if(form.is_valid()) :
            form.save();
            return redirect('addAlbumPage');
    else :
        form = forms.AlbumForm();
    return render(request, 'addAlbum.html', {"form" : addForm});

# Create your views here.
def listAlbums(request) :
    data = models.Album.objects.all();
    return render(request, 'albums.html', {"data" : data});

# Create your views here.
def editAlbum(request) :
    return render(request, 'editAlbum.html');
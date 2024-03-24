from django.shortcuts import render
from . import forms;

# Create your views here.
def addMusician(request) :
    addForm = forms.AlbumForm;
    return render(request, 'addMusician.html', {"form" : addForm});

# Create your views here.
def listMusicians(request) :
    return render(request, 'musicians.html');

# Create your views here.
def editMusician(request) :
    return render(request, 'editMusician.html');

# Create your views here.
def addAlbum(request) :
    return render(request, 'addAlbum.html');

# Create your views here.
def listAlbums(request) :
    return render(request, 'albums.html');

# Create your views here.
def editAlbum(request) :
    return render(request, 'editAlbum.html');
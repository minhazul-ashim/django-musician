from django import forms;
from . import models;
import datetime;

class MusicianForm(forms.ModelForm) :
    class Meta :
        model = models.Musician;
        fields = "__all__";

class AlbumForm(forms.ModelForm) :
    class Meta :
        model = models.Album;
        fields = "__all__";
        widgets = {
            "releaseDate": forms.DateInput(attrs={'type': 'date'})
        }
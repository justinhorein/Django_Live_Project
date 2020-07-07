from django.forms import ModelForm
from .models import Song


# Create the form class.
class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'
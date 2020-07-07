from django.forms import ModelForm
from .models import TravelList


# Create the form class.
class TravelForm(ModelForm):
    class Meta:
        model = TravelList
        fields = '__all__'
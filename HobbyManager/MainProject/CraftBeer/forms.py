from django.forms import ModelForm
from .models import Beer


# Create the form class
class BeerForm(ModelForm):
    class Meta:
        model = Beer
        fields = '__all__'

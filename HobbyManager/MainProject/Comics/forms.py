from django import forms
from .models import Books


# Create the form class.
class ComicForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

from django.forms import ModelForm
from .models import Deck

class NewDeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = ['deck_name']

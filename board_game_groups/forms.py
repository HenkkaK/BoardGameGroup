from django import forms

from .models import Game, Borrow

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'owner', 'description', 'is_borrowed']
        labels = {'name': 'Name of the game', 'owner': 'Owner of the game', 'description' : 'Description', 'is_borrowed' : 'Borrowed'}

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow

    # täytyy keksiä mitä kenttiä tähän tulee
        fields = ['contact_information', 'planned_return_date']
        labels = {'contact_information' : 'Contact information', 'planned_return_date' : 'planned return date'}
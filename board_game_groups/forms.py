from django import forms

from .models import Game, Borrow

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['Game_name', 'Owner', 'Game_description', 'is_borrowed']
        labels = {'Game_name': 'Name of the game', 'Owner': 'Owner of the game', 'Game_description' : 'Description', 'is_borrowed' : 'Borrowed'}

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow

    # täytyy keksiä mitä kenttiä tähän tulee
        fields = ['Contact_information', 'Planned_return_date']
        labels = {'Contact_information' : 'Contact_information', 'Planned_return_date' : 'Planned_return_date'}
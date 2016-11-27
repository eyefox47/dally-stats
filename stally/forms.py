from django import forms
from .models import Pokemon


class PokemonForm(forms.ModelForm):

    class Meta:
        model = Pokemon
        fields = ('name', 'player', 'campaign', 'pronouns', 'pokedex_nr',
                  'kind', 'type_p', 'trainer', 'nature', 'description')

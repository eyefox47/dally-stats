from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Pokemon, Character, Pet


class PokemonForm(forms.ModelForm):

    class Meta:
        model = Pokemon
        fields = ('image', 'name', 'player', 'campaign', 'pronouns',
                  'pokedex_nr', 'kind', 'type_p',
                  'trainer', 'nature', 'description')


class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = ('image', 'name', 'player', 'campaign', 'pronouns',
                  'character_class', 'description')


class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = ('image', 'name', 'player', 'trainer', 'campaign', 'pronouns',
                  'character_class', 'description')


class NPCForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = ('image', 'name', 'campaign', 'pronouns',
                  'character_class', 'description')


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_active = False

        if commit:
            user.save()

        return user

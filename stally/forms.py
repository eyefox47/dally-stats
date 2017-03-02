from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Pokemon, Character, Pet, Campaign


class PokemonForm(forms.ModelForm):

    class Meta:
        model = Pokemon
        fields = ('image', 'name', 'player', 'campaign', 'pronouns',
                  'pokedex_nr', 'kind', 'type_p',
                  'trainer', 'nature', 'description')


class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign
        fields = ('image', 'name', 'dm', 'start_date', 'youtube_playlist',
                  'description', 'end_date')


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

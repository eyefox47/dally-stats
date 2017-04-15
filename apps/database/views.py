from django.shortcuts import render, \
     get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from .models import Campaign, Character, Pokemon, Player, Pet
from .forms import PokemonForm, CharacterForm, NPCForm, PetForm, \
    CampaignForm, MyRegistrationForm


# List views


def campaign_list(request):
    campaigns = Campaign.objects.all().order_by('start_date').reverse()
    return render(request, 'database/list_pages/campaign_list.html',
                  {'campaigns': campaigns})


def campaign_character_list(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    characters = campaign.characters_without_trainees().exclude(
        pk__in=campaign.npcs())
    return render(request, 'database/list_pages/campaign_character_list.html',
                  {'campaign': campaign, 'characters': characters})


def character_pokemon_list(request, pk):
    character = get_object_or_404(Character, pk=pk)
    pokemons = character.pokemons
    return render(request, 'database/list_pages/character_pokemon_list.html',
                  {'character': character, 'pokemons': pokemons})


def character_pet_list(request, pk):
    character = get_object_or_404(Character, pk=pk)
    pets = character.pets
    return render(request, 'database/list_pages/character_pet_list.html',
                  {'character': character, 'pets': pets})


def campaign_pokemon_list(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    pokemons = campaign.pc_pokemon()
    return render(request, 'database/list_pages/campaign_pokemon_list.html',
                  {'campaign': campaign, 'pokemons': pokemons})


def campaign_npc_list(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    return render(request, 'database/list_pages/campaign_npc_list.html',
                  {'campaign': campaign})


# Detail views


def campaign_detail(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    return render(request, 'database/detail_pages/campaign_detail.html',
                  {'campaign': campaign})


def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return render(request, 'database/detail_pages/character_detail.html',
                  {'character': character})


def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'database/detail_pages/pet_detail.html',
                  {'pet': pet})


def pokemon_detail(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    return render(request, 'database/detail_pages/pokemon_detail.html',
                  {'pokemon': pokemon})


def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'database/detail_pages/player_detail.html',
                  {'player': player})


# Create and edit views


@method_decorator(login_required, name='dispatch')
class CharacterNew(CreateView):
    model = Character
    form_class = CharacterForm
    template_name = 'database/edit_pages/character_edit.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super(CharacterNew, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class CharacterEdit(UpdateView):
    model = Character
    form_class = CharacterForm
    template_name = 'database/edit_pages/character_edit.html'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user
        return super(CharacterEdit, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class NPCNew(CreateView):
    model = Character
    form_class = NPCForm
    template_name = 'database/edit_pages/npc_edit.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        character = form.save(commit=False)
        character.player = character.campaign.dm
        character.save()
        return super(NPCNew, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class PokemonNew(CreateView):
    model = Pokemon
    form_class = PokemonForm
    template_name = 'database/edit_pages/pokemon_edit.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super(PokemonNew, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class PokemonEdit(UpdateView):
    model = Pokemon
    form_class = PokemonForm
    template_name = 'database/edit_pages/pokemon_edit.html'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user
        return super(PokemonEdit, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class CampaignNew(CreateView):
    model = Campaign
    form_class = CampaignForm
    template_name = 'database/edit_pages/campaign_edit.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super(CampaignNew, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class CampaignEdit(UpdateView):
    model = Campaign
    form_class = CampaignForm
    template_name = 'database/edit_pages/campaign_edit.html'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user
        return super(CampaignEdit, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class PetNew(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'database/edit_pages/pet_edit.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super(PetNew, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class PetEdit(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'database/edit_pages/pet_edit.html'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user
        return super(PetEdit, self).form_valid(form)


class Register(CreateView):
    form_class = MyRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('registration_complete')


# Static views

def start(request):
    return render(request, 'database/start.html', {})


def about(request):
    return render(request, 'database/about.html', {})


def registration_complete(request):
    return render(request, 'registration/registration_complete.html')

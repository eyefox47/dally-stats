from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Campaign, Character, Pokemon, Player
from .forms import PokemonForm


def campaign_list(request):
    campaigns = Campaign.objects.all().order_by('start_date').reverse()
    return render(request, 'stally/list_pages/campaign_list.html',
                  {'campaigns': campaigns})


def campaign_character_list(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    characters = campaign.characters_without_pokemon().exclude(
        pk__in=campaign.npcs())
    return render(request, 'stally/list_pages/campaign_character_list.html',
                  {'campaign': campaign, 'characters': characters})


def character_pokemon_list(request, pk):
    character = get_object_or_404(Character, pk=pk)
    pokemons = character.pokemons
    return render(request, 'stally/list_pages/character_pokemon_list.html',
                  {'character': character, 'pokemons': pokemons})


def campaign_pokemon_list(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    pokemons = campaign.pc_pokemon()
    return render(request, 'stally/list_pages/campaign_pokemon_list.html',
                  {'campaign': campaign, 'pokemons': pokemons})


def campaign_npc_list(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    return render(request, 'stally/list_pages/campaign_npc_list.html',
                  {'campaign': campaign})


def campaign_detail(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    return render(request, 'stally/detail_pages/campaign_detail.html',
                  {'campaign': campaign})


def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return render(request, 'stally/detail_pages/character_detail.html',
                  {'character': character})


def pokemon_detail(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    return render(request, 'stally/detail_pages/pokemon_detail.html',
                  {'pokemon': pokemon})


@login_required
def pokemon_new(request):
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            pokemon = form.save(commit=False)

            pokemon.save()
            return redirect('pokemon_detail', pk=pokemon.pk)
    else:
        form = PokemonForm()
    return render(request, 'stally/edit_pages/pokemon_edit.html',
                  {'form': form})


@login_required
def pokemon_edit(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == "POST":
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            pokemon = form.save(commit=False)

            pokemon.save()
            return redirect('pokemon_detail', pk=pokemon.pk)
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'stally/edit_pages/pokemon_edit.html',
                  {'form': form})


def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'stally/detail_pages/player_detail.html',
                  {'player': player})


def about(request):
    return render(request, 'stally/about.html', {})

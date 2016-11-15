from django.shortcuts import render, get_object_or_404
from .models import Campaign, Character, Pokemon, Player

def campaign_list(request):
    campaigns = Campaign.objects.all().order_by('start_date').reverse()
    return render(request, 'stally/campaign_list.html', {'campaigns': campaigns})

def campaign_character_list(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    characters = campaign.characters_without_pokemon().exclude(pk__in=campaign.npcs())
    return render(request, 'stally/campaign_character_list.html', {'campaign': campaign, 'characters': characters})

def character_pokemon_list(request, pk):
    character = get_object_or_404(Character, pk=pk)
    pokemons = character.pokemons
    return render(request, 'stally/character_pokemon_list.html', {'character': character, 'pokemons': pokemons})

def campaign_pokemon_list(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    pokemons = campaign.pc_pokemon()
    return render(request, 'stally/campaign_pokemon_list.html', {'campaign': campaign, 'pokemons': pokemons})

def campaign_npc_list(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    return render(request, 'stally/campaign_npc_list.html', {'campaign': campaign})

def campaign_detail(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    return render(request, 'stally/campaign_detail.html', {'campaign': campaign})

def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return render(request, 'stally/character_detail.html', {'character': character})

def pokemon_detail(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    return render(request, 'stally/pokemon_detail.html', {'pokemon': pokemon})

def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'stally/player_detail.html', {'player': player})

def about(request):
    return render(request, 'stally/about.html', {})

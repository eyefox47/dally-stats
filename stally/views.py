from django.shortcuts import render, get_object_or_404
from .models import Campaign, Character

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
    pokemons = campaign.pokemons()
    return render(request, 'stally/campaign_pokemon_list.html', {'campaign': campaign, 'pokemons': pokemons})

def campaign_npc_list(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    return render(request, 'stally/campaign_npc_list.html', {'campaign': campaign})

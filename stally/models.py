# This Python file uses the following encoding: utf-8

from django.db import models
from django.utils import timezone
from django.core.validators import validate_comma_separated_integer_list
from datetime import timedelta


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Player(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/players/',
                              default='images/no-img.jpg')

    def main_characters(self):
        characters = Character.objects.filter(player=self)
        trainees = Trainee.objects.filter(player=self)
        campaigns = Campaign.objects.filter(dm=self)
        npcs = Character.objects.filter(campaign__in=campaigns)
        return characters.exclude(pk__in=trainees).exclude(pk__in=npcs)

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.name < other.name

    class Meta:
        ordering = ['name']


class Campaign(BaseModel):
    name = models.CharField(max_length=200)
    dm = models.ForeignKey(Player, on_delete=models.PROTECT,
                           related_name='campaigns_dming', verbose_name='DM')
    start_date = models.DateField(default=timezone.now,
                                  verbose_name='Start date')
    image = models.ImageField(upload_to='images/campaigns/',
                              default='images/no-img.jpg')
    youtube_playlist = models.URLField(blank=True, null=True,
                                       verbose_name='YouTube playlist')
    description = models.TextField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True,
                                verbose_name='End date')

    def players(self):
        characters = Character.objects.filter(campaign=self)
        return sorted(set(Player.objects.filter(
            characters__in=characters).exclude(name=self.dm.name)))

    def characters_without_trainees(self):
        characters = Character.objects.filter(
            campaign=self).exclude(pk__in=self.npcs())
        trainees = Trainee.objects.filter(campaign=self)

        return characters.exclude(pk__in=trainees)

    def pc_pokemon(self):
        return Pokemon.objects.filter(campaign=self).exclude(player=self.dm)

    def npcs(self):
        characters = Character.objects.filter(campaign=self)
        pokemon = Pokemon.objects.filter(campaign=self)
        return characters.filter(player=self.dm).exclude(pk__in=pokemon)

    def npc_pokemon(self):
        pokemon = Pokemon.objects.filter(campaign=self)
        return pokemon.filter(player=self.dm)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Session(BaseModel):
    name = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE,
                                 related_name='sessions')
    length = models.DurationField(default=timedelta(0))
    number = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    players_present = models.ManyToManyField(Player, blank=True)

    def __str__(self):
        return "{}. {}".format(self.number, self.name)

    class Meta:
        ordering = ['name']


class URL(BaseModel):
    link = models.URLField()
    session = models.ForeignKey(Session, on_delete=models.CASCADE,
                                related_name='youtube_videos')


class Place(BaseModel):
    name = models.CharField(max_length=400)
    campaigns = models.ManyToManyField(Campaign)
    description = models.TextField(blank=True, null=True)


class Character(BaseModel):
    name = models.CharField(max_length=100)
    player = models.ForeignKey(Player, on_delete=models.PROTECT,
                               related_name='characters')
    campaign = models.ForeignKey(Campaign, on_delete=models.PROTECT,
                                 related_name='characters')
    character_class = models.CharField(max_length=200, blank=True, null=True,
                                       verbose_name='Class')
    image = models.ImageField(upload_to='images/characters/',
                              default='images/no-img.jpg')
    pronouns = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    lives_in = models.ManyToManyField(Place, blank=True,
                                      related_name='citizens')
    in_campaign_since = models.ForeignKey(Session, on_delete=models.SET_NULL,
                                          blank=True, null=True)

    def pokemons(self):
        return Pokemon.objects.filter(trainer=self)

    def pets(self):
        return Pet.objects.filter(trainer=self)

    def is_npc(self):
        return self.player == self.campaign.dm

    def __str__(self):
        if self.is_npc():
            return '{} (NPC)'.format(self.name)
        else:
            return '{} (played by {})'.format(self.name, self.player.name)

    class Meta:
        ordering = ['name']


class Trainee(Character):
    trainer = models.ForeignKey(
        Character, on_delete=models.SET_NULL, related_name='trainees',
        blank=True, null=True)


class Pokemon(Trainee):
    pokedex_nr = models.CharField(
        max_length=7, blank=True, null=True,
        validators=[validate_comma_separated_integer_list],
        verbose_name='Pokédex number')
    type_p = models.CharField(max_length=200, verbose_name='Type')
    nature = models.CharField(max_length=200, blank=True, null=True)
    kind = models.CharField(max_length=200)

    def create_pokemon(character, name, pokedex_nr, type_p, nature, kind):
        new_pokemon = Pokemon(name=name, player=character.player,
                              campaign=character.campaign,
                              pokedex_nr=pokedex_nr,
                              trainer=character,
                              type_p=type_p, nature=nature, kind=kind)
        new_pokemon.save()

    class Meta:
        ordering = ['name']
        verbose_name = 'Pokémon'
        verbose_name_plural = 'Pokémon'


class Pet(Trainee):
    pass

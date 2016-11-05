from django.db import models
from django.utils import timezone


class Player(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'images/players/', default = 'images/no-img.jpg')

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.name < other.name

    class Meta:
        ordering = ['name']

class Campaign(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'images/campaigns/', default = 'images/no-img.jpg')
    dm = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='campaigns_dming')
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)

    def players(self):
        characters = Character.objects.filter(campaign=self)
        return sorted(set(Player.objects.filter(characters__in=characters).exclude(name=self.dm.name)))

    def characters_without_pokemon(self):
        characters = Character.objects.filter(campaign=self)
        pokemon = Pokemon.objects.filter(campaign=self)

        return characters.exclude(pk__in=pokemon)

    def pokemons(self):
        return Pokemon.objects.filter(campaign=self)

    def npcs(self):
        characters = Character.objects.filter(campaign=self)
        return characters.filter(player=self.dm)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Session(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='sessions')
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return "{}. {}".format(self.number, self.name)

    class Meta:
        ordering = ['name']

class Character(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'images/characters/', default = 'images/no-img.jpg')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='characters')
    pronouns = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='characters')
    in_campaign_since = models.ForeignKey(Session, on_delete=models.CASCADE, blank=True, null=True)

    def is_npc(self):
        return self.player == self.campaign.dm

    def __str__(self):
        if self.is_npc():
            return '{} (NPC)'.format(self.name)
        else:
            return '{} (played by {})'.format(self.name, self.player.name)

    class Meta:
        ordering = ['name']

class Pokemon(Character):
    trainer = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='pokemons', blank=True, null=True)
    type_p = models.CharField(max_length=200)
    nature = models.CharField(max_length=200, blank=True, null=True)
    kind = models.CharField(max_length=200)

    def create_pokemon(character, name, type_p, kind):
        new_pokemon = Pokemon(name=name,
            player=character.player, campaign=character.campaign,
            trainer=character, type_p=type_p, kind=kind)
        new_pokemon.save()

    class Meta:
        ordering = ['name']
        verbose_name = 'Pokémon'
        verbose_name_plural = 'Pokémon'

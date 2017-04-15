from django.contrib import admin
from .models import Player, Campaign, Character, Pokemon, Session, Pet


class CampaignAdmin(admin.ModelAdmin):
    pass


class CharacterAdmin(admin.ModelAdmin):
    pass


class PokemonAdmin(admin.ModelAdmin):
    pass


class SessionAdmin(admin.ModelAdmin):
    pass


class PetAdmin(admin.ModelAdmin):
    pass


admin.site.register(Player)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Pet, PetAdmin)

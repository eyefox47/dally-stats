from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.campaign_list, name='campaign_list'),
    url(r'^campaign/(?P<pk>\d+)/characters/$', views.campaign_character_list, name='campaign_character_list'),
    url(r'^characters/(?P<pk>\d+)/pokemon/$', views.character_pokemon_list, name='character_pokemon_list'),
    url(r'^campaign/(?P<pk>\d+)/pokemon/$', views.campaign_pokemon_list, name='campaign_pokemon_list'),
    url(r'^campaign/(?P<pk>\d+)/npcs/$', views.campaign_npc_list, name='campaign_npc_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

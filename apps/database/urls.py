from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as django_views
from . import views
from apps.database.views import CharacterNew

urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^campaigns$', views.campaign_list, name='campaign_list'),
    url(r'^campaigns/(?P<pk>\d+)/characters/$', views.campaign_character_list,
        name='campaign_character_list'),
    url(r'^campaigns/(?P<pk>\d+)/$',
        views.campaign_detail, name='campaign_detail'),
    url(r'^characters/(?P<pk>\d+)/pokemon/$', views.character_pokemon_list,
        name='character_pokemon_list'),
    url(r'^characters/(?P<pk>\d+)/pets/$', views.character_pet_list,
        name='character_pet_list'),
    url(r'^characters/(?P<pk>\d+)/$', views.character_detail,
        name='character_detail'),
    url(r'^pets/(?P<pk>\d+)/$', views.pet_detail, name='pet_detail'),
    url(r'^pets/(?P<pk>\d+)/edit/$', views.PetEdit.as_view(),
        name='pet_edit'),
    url(r'^pets/new/$', views.PetNew.as_view(),
        name='pet_new'),
    url(r'^characters/new/$', views.CharacterNew.as_view(),
        name='character_new'),
    url(r'^characters/(?P<pk>\d+)/edit/$', views.CharacterEdit.as_view(),
        name='character_edit'),
    url(r'^npc/new/$', views.NPCNew.as_view(), name='npc_new'),
    url(r'^campaigns/(?P<pk>\d+)/pokemon/$', views.campaign_pokemon_list,
        name='campaign_pokemon_list'),
    url(r'^campaigns/(?P<pk>\d+)/npcs/$', views.campaign_npc_list,
        name='campaign_npc_list'),
    url(r'^pokemon/(?P<pk>\d+)/$', views.pokemon_detail,
        name='pokemon_detail'),
    url(r'^pokemon/new/$', views.PokemonNew.as_view(), name='pokemon_new'),
    url(r'^pokemon/(?P<pk>\d+)/edit/$', views.PokemonEdit.as_view(),
        name='pokemon_edit'),
    url(r'^campaigns/new/$', views.CampaignNew.as_view(), name='campaign_new'),
    url(r'^campaigns/(?P<pk>\d+)/edit/$', views.CampaignEdit.as_view(),
        name='campaign_edit'),
    url(r'^players/(?P<pk>\d+)/$', views.player_detail, name='player_detail'),
    url(r'^about/$', views.about, name='about'),
    url(r'^accounts/login/$', django_views.login, name='login'),
    url(r'^accounts/logout/$', django_views.logout,
        name='logout', kwargs={'next_page': '/campaigns'}),
    # Registration URLs
    url(r'^accounts/register/$', views.Register.as_view(), name='register'),
    url(r'^accounts/register/complete/$',
        views.registration_complete,
        name='registration_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

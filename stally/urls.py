from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as django_views
from . import views

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
    url(r'^pets/(?P<pk>\d+)/edit/$', views.pet_edit,
        name='pet_edit'),
    url(r'^characters/new/$', views.character_new, name='character_new'),
    url(r'^characters/(?P<pk>\d+)/edit/$', views.character_edit,
        name='character_edit'),
    url(r'^npc/new/$', views.npc_new, name='npc_new'),
    url(r'^campaigns/(?P<pk>\d+)/pokemon/$', views.campaign_pokemon_list,
        name='campaign_pokemon_list'),
    url(r'^campaigns/(?P<pk>\d+)/npcs/$', views.campaign_npc_list,
        name='campaign_npc_list'),
    url(r'^pokemon/(?P<pk>\d+)/$', views.pokemon_detail,
        name='pokemon_detail'),
    url(r'^pokemon/new/$', views.pokemon_new, name='pokemon_new'),
    url(r'^pokemon/(?P<pk>\d+)/edit/$', views.pokemon_edit,
        name='pokemon_edit'),
    url(r'^campaigns/new/$', views.campaign_new, name='campaign_new'),
    url(r'^campaigns/(?P<pk>\d+)/edit/$', views.campaign_edit,
        name='campaign_edit'),
    url(r'^players/(?P<pk>\d+)/$', views.player_detail, name='player_detail'),
    url(r'^about/$', views.about, name='about'),
    url(r'^accounts/login/$', django_views.login, name='login'),
    url(r'^accounts/logout/$', django_views.logout,
        name='logout', kwargs={'next_page': '/campaigns'}),
    # Registration URLs
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/register/complete/$',
        views.registration_complete,
        name='registration_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

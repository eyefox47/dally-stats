from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
import urllib.request, unicodedata, os
from shutil import copyfileobj
from stally.models import Pokemon
from django.conf import settings

class Command(BaseCommand):
    help = 'If there is no image set for a Pokemon, this will attempt to get a default image based on the Pokedex number(s).'

    def handle(self, *args, **options):

        pokemons = Pokemon.objects.all()

        for pokemon in pokemons:
            if pokemon.image.url == '/media/images/no-img.jpg' and pokemon.pokedex_nr:
                number = pokemon.pokedex_nr.partition(',')
                print("Pokemon {} has no image.".format(pokemon.name))

                if number[1] == '' and number[2] == '': # Is not a fusion
                    print('{} is not a fusion. grabbing image...'.format(pokemon.name))
                    name = unicodedata.normalize('NFKD', pokemon.kind).encode('ascii', 'ignore').decode('utf-8').lower()
                    url = "https://img.pokemondb.net/artwork/{}.jpg".format(name)
                    self.set_image(url, pokemon)
                elif len(number) == 3: # Is a fusion of two Pokemon
                    print('{} is a fusion of {} and {}. Grabbing fusion image...'.format(pokemon.name, number[0], number[2]))
                    url = "http://images.alexonsager.net/pokemon/fused/{0}/{0}.{1}.png".format(number[0], number[2])
                    self.set_image(url, pokemon)

    def set_image(self, url, pokemon):
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8'
        }
        try:
            request = urllib.request.Request(url, headers=hdr)
            file_name = os.path.basename(url)
            path = os.path.join(settings.MEDIA_ROOT, file_name)
            with urllib.request.urlopen(request) as in_stream, open(path, 'wb') as out_file:
                copyfileobj(in_stream, out_file)

            pokemon.image = File(open(path, 'rb'))
            pokemon.save()

            os.remove(os.path.join(settings.MEDIA_ROOT, file_name))

            print('Success. new image is {}'.format(url))
        except urllib.error.HTTPError:
            print('No valid image found. tried {}'.format(url))

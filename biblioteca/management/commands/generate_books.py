import os
import django
from django.core.management.base import BaseCommand
from faker import Faker
from biblioteca.models import Llibre, Pais, Llengua,Exemplar

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

class Command(BaseCommand):
    help = 'Genera libros en catalán, inglés y alemán'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Crear países y lenguas
        pais_catalan = Pais.objects.create(nom="España")
        pais_ingles = Pais.objects.create(nom="Estados Unidos")
        pais_aleman = Pais.objects.create(nom="Alemania")

        llengua_catalan = Llengua.objects.create(nom="Català")
        llengua_ingles = Llengua.objects.create(nom="English")
        llengua_aleman = Llengua.objects.create(nom="Deutsch")

        # Generar 10 libros en catalán
        for _ in range(10):
            newLlibre = Llibre.objects.create(
                titol=fake.sentence(nb_words=4),
                autor=fake.name(),
                pais=pais_catalan,
                llengua=llengua_catalan,
                editorial=fake.company(),
                data_edicio=fake.date_between(start_date='-30y', end_date='today'),
                resum=fake.text(max_nb_chars=200)
            )
            Exemplar.objects.create(cataleg=newLlibre)
            Exemplar.objects.create(cataleg=newLlibre)

        # Generar 10 libros en inglés
        for _ in range(10):
            newLlibre= Llibre.objects.create(
                titol=fake.sentence(nb_words=4),
                autor=fake.name(),
                pais=pais_ingles,
                llengua=llengua_ingles,
                editorial=fake.company(),
                data_edicio=fake.date_between(start_date='-30y', end_date='today'),
                resum=fake.text(max_nb_chars=200)
            )
            Exemplar.objects.create(cataleg=newLlibre)
            Exemplar.objects.create(cataleg=newLlibre)

        # Generar 10 libros en alemán
        for _ in range(10):
            newLlibre = Llibre.objects.create(
                titol=fake.sentence(nb_words=4),
                autor=fake.name(),
                pais=pais_aleman,
                llengua=llengua_aleman,
                editorial=fake.company(),
                data_edicio=fake.date_between(start_date='-30y', end_date='today'),
                resum=fake.text(max_nb_chars=200)
            )
            Exemplar.objects.create(cataleg=newLlibre)
            Exemplar.objects.create(cataleg=newLlibre)


        self.stdout.write(self.style.SUCCESS('Libros generados exitosamente'))
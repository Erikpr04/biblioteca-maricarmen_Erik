import os
from django.core.management.base import BaseCommand
from biblioteca.models import Usuari
from faker import Faker

class Command(BaseCommand):
    help = 'Genera usuarios falsos para el panel de administración'

    def add_arguments(self, parser):
        parser.add_argument(
            'total',
            type=int,
            help='Número de usuarios a generar'
        )

    def handle(self, *args, **kwargs):
        fake = Faker()
        total = kwargs['total']

        for _ in range(total):
            # Generar datos falsos
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = f"{first_name.lower()}_{last_name.lower()}"
            email = fake.email()
            password = fake.password(length=12)

            # Crear el usuario
            user = Usuari.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )

            self.stdout.write(self.style.SUCCESS(f'Usuario creado: {username}'))

        self.stdout.write(self.style.SUCCESS(f'Se han creado {total} usuarios exitosamente'))
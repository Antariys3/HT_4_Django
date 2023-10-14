import random

from django.core.management.base import BaseCommand
from faker import Faker

from st_app.models import Teacher

fake = Faker("ru_RU")

ext_word_list = [
    "Математика",
    "Литература",
    "История",
    "Биология",
    "Химия",
    "Физика",
    "География",
    "Информатика",
    "Иностранный язык",
    "Музыка",
    "Изобразительное искусство",
    "Физическая культура",
    "Обществознание",
    "Технология",
    "Украинский язык",
    "Экономика",
    "Психология",
    "Хореография",
    "Астрономия",
    "Этика",
]


class Command(BaseCommand):
    help = "Add the specified number of teacher to the database"

    def add_arguments(self, parser):
        parser.add_argument("number", nargs="?", type=int, default=100)

    def handle(self, *args, **options):
        for number_of_teachers in range(options["number"]):
            teacher = Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                birth_date=fake.date_of_birth(minimum_age=25, maximum_age=60),
                subject=random.choice(ext_word_list),
            )

            self.stdout.write(
                self.style.SUCCESS('Successfully added teacher "%s"' % teacher.id)
            )

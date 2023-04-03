from django.core.management import BaseCommand
from django.utils.crypto import get_random_string

from apps.common.models import State, Province, Country, Area
from apps.stock.models import Brand


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = "oil.csv"
        with open(file_path, 'r') as file:
            # india = Country.objects.get_obj_from_code("IN")
            # up = State.objects.filter(code="UP").first()
            # lucknow = Province.objects.filter(name="Lucknow").first()

            raw_data = file.read()
            all_lines = raw_data.split('\n')
            for line in all_lines:
                Brand.objects.create(name=line, code=get_random_string(length=4).upper())
                # obj = line.split(",")
                # if len(obj) == 2:
                #     Area.objects.create(name=obj[0], code="", zip_code=obj[1], province=lucknow)


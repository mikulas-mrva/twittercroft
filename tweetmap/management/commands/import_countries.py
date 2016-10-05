from django.core.management.base import BaseCommand, CommandError
from tweetmap.models import Country
import csv


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        self.stdout.write(options['filename'])

        try:
            with open(options['filename'], 'r') as country_data:
                rows = csv.reader(country_data, delimiter=",", quotechar='"')

                for row in rows:
                    if rows.line_num == 1:
                        continue

                    if len(row):
                        country_name = row[0]
                        country_code = row[1]
                        country_camel_case_name = ''.join(map(
                            lambda s: s[0].upper() + s[1:],
                            row[0].split(' ')
                        ))
                        country_lng = None if row[2] == 'None' else row[2]
                        country_lat = None if row[3] == 'None' else row[3]

                        _, created = Country.objects.get_or_create(
                            name=country_name,
                            code=country_code,
                            camel_case_name=country_camel_case_name,
                            lng=country_lng,
                            lat=country_lat,
                        )

                        if created:
                            self.stdout.write('Successfully imported {}.'.format(row[0]))

        except FileNotFoundError:
            self.stderr.write('File does not exist: {}'.format(options['filename']))
        else:
            self.stdout.write(self.style.SUCCESS('Import complete.'))

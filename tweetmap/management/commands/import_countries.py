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

                    _, created = Country.objects.get_or_create(
                        name=row[0],
                        code=row[1],
                        lng=row[2],
                        lat=row[3],
                    )

                    if created:
                        self.stdout.write('Successfully added {}.'.format(row[0]))
        except FileNotFoundError:
            self.stderr.write('File does not exist: {}'.format(options['filename']))
        else:
            self.stdout.write(self.style.SUCCESS('Import complete.'))

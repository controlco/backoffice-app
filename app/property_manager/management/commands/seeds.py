from django.core.management.base import BaseCommand
from app.factories import UserFactory, PropertyFactory, ReportFactory


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--n',
                            default=20,
                            type=int,
                            help='The number to create.')

    def handle(self, *args, **options):
        for _ in range(options['n']):
            UserFactory.create()
            PropertyFactory.create()
            ReportFactory.create()

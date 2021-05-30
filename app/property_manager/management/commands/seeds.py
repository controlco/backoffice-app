from django.core.management.base import BaseCommand
from app.factories import UserFactory, PropertyFactory, ReportFactory
from random import choice
from accounts.models import User, Report
from property_manager.models import Property, District


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
            PropertyFactory.create(owner=choice(
                User.objects.all()), district=choice(District.objects.all()))
            ReportFactory.create(owner=choice(
                User.objects.all()), reported_user=choice(list(User.objects.all())))

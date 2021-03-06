
from accounts.models import User, Report
import factory
from factory.django import DjangoModelFactory
from property_manager.models import Property, District
from random import choice, randint


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    rut = "111111111"
    birth_date = factory.Faker("date_of_birth")
    is_active = factory.Faker("boolean")
    password = "pbkdf2_sha256$260000$LtWXw7g3Idd2xUp4vX6H1n$6FVefdXrDEy/rMGY1iWIrrFpEm2HPvKgWxpRCdeJzTM="
    if is_active:
        is_owner = False
    else:
        is_owner = True


class PropertyFactory(DjangoModelFactory):
    class Meta:
        model = Property

    owner = choice(list(User.objects.all()))
    title = factory.Faker('sentence')
    surface = factory.Faker('random_int')
    adress = factory.Faker('address')
    price = factory.Faker('random_int')
    description = factory.Faker('paragraph')
    latitude = factory.Faker('random_int')
    longitude = factory.Faker('random_int')
    district = choice(District.objects.all())


class ReportFactory(DjangoModelFactory):
    class Meta:
        model = Report

    title = factory.Faker('sentence')
    content = factory.Faker('paragraph')
    owner = choice(list(User.objects.all()))
    reported_user = factory.SubFactory(UserFactory)

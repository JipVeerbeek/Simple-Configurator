import factory
from faker import Faker

from products import factories

from . import models

fake = Faker()

# number = fake.random_int(min=1000, max=9999)
# letters = fake.random_uppercase_letter() + fake.random_uppercase_letter()


class ConfigurationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Configuration

    product = factory.SubFactory(factories.ProductFactory)
    address = factory.LazyAttribute(lambda o: AddressFactory() if fake.boolean() else None)
    status = "draft"


class ConfigurationLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ConfigurationLine
        django_get_or_create = ["product_question_article", "configuration"]

    product_question_article = factory.SubFactory(factories.ProductQuestionArticleFactory)
    configuration = factory.SubFactory(ConfigurationFactory)


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Address
        django_get_or_create = ["first_name", "middle_name", "address"]

    first_name = factory.Faker("first_name")
    middle_name = factory.LazyAttribute(lambda o: fake.name() if fake.boolean() else None)
    last_name = factory.Faker("last_name")
    address = factory.Faker("address")
    # postal_code = f"{number}{letters}"
    city = factory.Faker("city")

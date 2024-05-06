import factory
from . import models
from faker import Faker
from products import factories

fake = Faker()


class ConfigurationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Configuration

    product_id = factory.SubFactory(factories.ProductFactory)
    address_id = factory.LazyAttribute(lambda o: AddressFactory() if fake.boolean() else None)
    status = 'draft'


class ConfigurationLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ConfigurationLine

    product_question_article_id = factory.SubFactory(factories.ProductQuestionArticleFactory)
    configuration_id = factory.SubFactory(ConfigurationFactory)


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Address

    first_name = factory.Faker('first_name')
    middle_name = factory.LazyAttribute(lambda o: fake.name() if fake.boolean() else None)
    last_name = factory.Faker('last_name')
    address = factory.Faker('address')
    city = factory.Faker('city')

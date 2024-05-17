import factory
from . import models


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Article
        django_get_or_create = ['name']

    name = factory.Faker('word')

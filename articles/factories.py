import factory
from . import models

# Todo: python has a quite strong set of conventions.
#       After imports, double newline (all files)
class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Article
        django_get_or_create = ['name']

    name = factory.Faker('word')

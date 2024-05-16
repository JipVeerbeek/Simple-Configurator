import factory
from . import models

# Todo: python has a quite strong set of conventions.
#       After imports, double newline (all files)
class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Article
        # todo: django_get_or_create on 'name' to prevent duplicates

    name = factory.Faker('word')

import factory
from . import models

class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Article

    name = factory.Faker('word')

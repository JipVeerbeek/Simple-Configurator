import factory
from . import models

class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Question

    name = factory.Faker('word')

import factory
from . import models

class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Question
        django_get_or_create = ['name']
        
    name = factory.Faker('word')

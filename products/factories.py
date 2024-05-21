import factory

from articles.factories import ArticleFactory
from questions.factories import QuestionFactory

from . import models


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product
        django_get_or_create = ["name"]

    name = factory.Faker("word")


class ProductQuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductQuestion

    product = factory.SubFactory(ProductFactory)
    question = factory.SubFactory(QuestionFactory)


class ProductQuestionArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductQuestionArticle

    product_question = factory.SubFactory(ProductQuestionFactory)
    article = factory.SubFactory(ArticleFactory)
    price = factory.Faker("random_int", min=0, max=99)

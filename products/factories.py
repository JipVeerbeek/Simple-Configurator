import factory
from . import models
from questions.factories import QuestionFactory
from articles.factories import ArticleFactory

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    name = factory.Faker('word')


class ProductQuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductQuestion

    product_id = factory.SubFactory(ProductFactory)
    question_id = factory.SubFactory(QuestionFactory)


class ProductQuestionArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductQuestionArticle

    product_question_id = factory.SubFactory(ProductQuestionFactory)
    article_id = factory.SubFactory(ArticleFactory)
    price = factory.Faker('random_int', min=0, max=1000)

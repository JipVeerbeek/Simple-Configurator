from django.urls import reverse
from rest_framework import status
from django.test import TransactionTestCase

from configurations.factories import (
    ConfigurationFactory,
    ConfigurationLineFactory,
)
from products.factories import (
    ProductFactory,
    ProductQuestionArticleFactory,
    ProductQuestionFactory,
)
from questions.factories import QuestionFactory


class ArticleTests(TransactionTestCase):
    def test_get_articles(self):
        product = ProductFactory()
        question = QuestionFactory()
        product_question = ProductQuestionFactory(product=product, question=question)
        configuration = ConfigurationFactory(product=product)
        product_question_article = ProductQuestionArticleFactory(product_question=product_question)
        ConfigurationLineFactory(
            product_question_article=product_question_article,
            configuration=configuration,
        )

        url = reverse(
            "ArticleListView",
            kwargs={
                "configuration_id": configuration.id,
                "question_id": question.id,
            },
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from configurations.factories import ConfigurationFactory, ConfigurationLineFactory
from products.factories import (
    ProductFactory,
    ProductQuestionArticleFactory,
    ProductQuestionFactory,
)
from questions.factories import QuestionFactory


class ArticleTests(APITestCase):
    def test_get_articles(self):
        product = ProductFactory()
        question = QuestionFactory()
        product_question = ProductQuestionFactory(
            product_id=product, question_id=question
        )
        configuration = ConfigurationFactory(product_id=product)
        product_question_article = ProductQuestionArticleFactory(
            product_question_id=product_question
        )
        ConfigurationLineFactory(
            product_question_article_id=product_question_article,
            configuration_id=configuration,
        )

        url = reverse(
            "ArticleListView",
            kwargs={"configuration_id": configuration.id, "question_id": question.id},
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # todo: Lines are a little long. Can you configure your IDE to use max length
        #       120 line length and apply it throughout your code? Very useful for split
        #       screen.

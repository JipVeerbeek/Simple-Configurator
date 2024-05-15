from .models import ConfigurationLine
from products.models import ProductQuestionArticle
from rest_framework.response import Response


class PriceService:
    def __init__(self, configuration):
        self.configuration = configuration

    def getOrderLines(self):
        return ConfigurationLine.objects.filter(configuration_id=self.configuration)
    
    def calculateOrderPrice(self):
        lines = self.getOrderLines()
        price = 0

        for line in lines:
            product_question_article = ProductQuestionArticle.objects.get(id=line.product_question_article_id.id)
            price = price + product_question_article.price

        return Response(price)

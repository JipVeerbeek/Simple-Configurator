from .models import ConfigurationLine
from .serializers import ConfigurationLineSerializer
from products.models import ProductQuestionArticle


class PriceService:
    def __init__(self, configuration):
        self.configuration = configuration

    def getOrderLines(self):
        return ConfigurationLine.objects.filter(configuration_id=self.configuration)
    
    def calculateOrderPrice(self):
        lines = self.getOrderLines()

        serialized_lines = ConfigurationLineSerializer(lines, many=True)
        price = 0

        for line in serialized_lines.data:
            product_question_article = ProductQuestionArticle.objects.get(id=line['product_question_article_id'])
            price = price + product_question_article.price

        return price

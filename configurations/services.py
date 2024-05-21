from products.models import ProductQuestionArticle

from .models import ConfigurationLine


class PriceService:
    def __init__(self, configuration):
        self.configuration = configuration

    def get_order_lines(self):
        return ConfigurationLine.objects.filter(configuration=self.configuration)

    def calculate_order_price(self):
        lines = self.get_order_lines()
        price = 0

        for line in lines:
            product_question_article = ProductQuestionArticle.objects.get(id=line.product_question_article.id)
            price = price + product_question_article.price

        return price

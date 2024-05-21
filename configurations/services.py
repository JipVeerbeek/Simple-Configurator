from products.models import ProductQuestionArticle
from .models import ConfigurationLine, Configuration


class PriceService:
    def __init__(self, configuration_id):
        self.configuration = self.get_configuration(configuration_id=configuration_id)

    def get_configuration(self, configuration_id):
        return Configuration.objects.get(id=configuration_id)

    def get_order_lines(self):
        return ConfigurationLine.objects.filter(configuration=self.configuration)

    def calculate_order_price(self):
        lines = self.get_order_lines()
        price = 0
        for line in lines:
            product_question_article = ProductQuestionArticle.objects.get(id=line.product_question_article.id)
            price = price + product_question_article.price

        return price


class DiscountPriceService(PriceService):
    def calculate_discounted_price(self, **kwargs):
        order_price = kwargs['order_price']
        discounted_price = order_price * 0.9
        return discounted_price

    def calculate_order_price(self):
        postal_code = self.configuration.address.postal_code
        code = postal_code[:4]
        code = int(code)
        order_price = super().calculate_order_price()

        if code in range(8000, 8999):
            return self.calculate_discounted_price(order_price=order_price)
        else:
            return order_price

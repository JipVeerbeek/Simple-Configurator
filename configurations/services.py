from products.models import ProductQuestionArticle
from .models import ConfigurationLine, Configuration, Address


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


class DiscountPriceService(PriceService):
    def get_configuration(self):
        return Configuration.objects.get(id=self.configuration)

    def get_address(self):
        configuration = self.get_configuration()
        return Address.objects.get(id=configuration.address.id)

    def calculate_order_price(self):
        address = self.get_address()
        print(address.address, flush=True)

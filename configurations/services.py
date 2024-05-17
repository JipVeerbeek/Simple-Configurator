from .models import ConfigurationLine
from products.models import ProductQuestionArticle
from rest_framework.response import Response


# Todo: create unit test for PriceService. Unit tests test isolated parts of a
#       service or function.
# class PriceServiceTestCase(TestCase):
#     def setUp(self):
#         self.configuration = ConfigurationFactory()
#         self.lines = ConfigurationLineFactory.create_batch()
#
#     def test_get_order_lines(self):
#         lines = PriceService(...).get_order_lines()
#         # check if lines created during setup are in the result
#
#     def test_calculate_order_price(self):
#         price = Price(...).get_order_price()
#         # check price is equal to expected price

class PriceService:
    def __init__(self, configuration):
        self.configuration = configuration

    def get_order_lines(self):
        return ConfigurationLine.objects.filter(configuration_id=self.configuration)
    
    def calculate_order_price(self):
        lines = self.get_order_lines()
        price = 0

        for line in lines:
            product_question_article = ProductQuestionArticle.objects.get(id=line.product_question_article_id.id)
            price = price + product_question_article.price

        # todo: no need for response here, it's a service not a(n) (api)view
        return Response(price)


from .models import ConfigurationLine

class PriceService:
    def __init__(self, configuration):
        self.configuration = configuration

    def getOrderLines(self):
        return ConfigurationLine.objects.filter(configuration_id=self.configuration.id)
    
    def calculateOrderPrice(self):
        lines = self.getOrderLines()

        price = 0
        for line in lines:
            price = price + line.price
        return price

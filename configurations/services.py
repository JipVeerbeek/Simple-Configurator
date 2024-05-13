from .models import ConfigurationLine

class PriceService:
    def __init__(self, configuration):
        self.configuration = configuration

    def getOrderLines(self):
        print(self.configuration.id)
        return ConfigurationLine.objects.get(configuration_id=self.configuration.id)
    
    def calculateOrderPrice(self):
        lines = self.getOrderLines()

        print(lines)        
        # price = 0
        # for line in lines:
        #     price = line.price
        # return price

from django.db import models


class Adress(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Adresses"

    def __str__(self):
        return str(self.id)


class Configuration(models.Model):
    adress_id = models.ForeignKey('Adress', on_delete=models.CASCADE)
    product_id = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='draft')

    def __str__(self):
        return str(self.id)


class Configuration_line(models.Model):
    product_question_article_id = models.ForeignKey('products.Product_question_article', on_delete=models.CASCADE)
    configuration_id = models.ForeignKey('Configuration', on_delete=models.CASCADE)

from django.db import models


class Configuration(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    address = models.ForeignKey(
        "Address", on_delete=models.CASCADE, blank=True, null=True
    )
    status = models.CharField(max_length=100, default="draft")

    def __str__(self):
        id = str(self.id)
        return f"Configuration: ({id})"


class ConfigurationLine(models.Model):
    product_question_article = models.ForeignKey(
        "products.ProductQuestionArticle", on_delete=models.CASCADE
    )
    configuration = models.ForeignKey("Configuration", on_delete=models.CASCADE)


class Address(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        id = str(self.id)
        return f"Address: ({id})"

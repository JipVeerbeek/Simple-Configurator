from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Product_question(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    question_id = models.ForeignKey('questions.Question', on_delete=models.CASCADE)

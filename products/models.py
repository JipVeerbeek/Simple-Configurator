from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        id = str(self.id)
        name = str(self.name)
        return f"Product: {name} ({id})"
    

class ProductQuestion(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    question_id = models.ForeignKey('questions.Question', on_delete=models.CASCADE)

    def __str__(self):
        id = str(self.id)
        return f"ProductQuestion: ({id})"


class ProductQuestionArticle(models.Model):
    product_question_id = models.ForeignKey('ProductQuestion', on_delete=models.CASCADE)
    article_id = models.ForeignKey('articles.Article', on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        id = str(self.id)
        return f"ProductQuestionArticle: ({id})"

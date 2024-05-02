from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        id = str(self.id)
        name = str(self.name)
        return f"Article: {name} ({id})"

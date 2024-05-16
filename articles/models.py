from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        # todo: id is a built-in, a convention is to prefix it with an underscore:
        #       thus: `_id = str(self.id)
        id = str(self.id)
        name = str(self.name)
        # todo: but... There is no need to cast.
        #       f"Article: {self.name} ({self.id))"
        return f"Article: {name} ({id})"

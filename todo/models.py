from django.db import models

class Todomodel(models.Model):
    title = models.CharField(max_length=50)
    memo = models.TextField()

    def __str__(self):
        return str(self.id) + '.' + self.title
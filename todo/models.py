from django.db import models

CHOICE = ('danger','high'), ('warning', 'normal'), ('primary', 'row')

class Todomodel(models.Model):
    title = models.CharField(max_length=50)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices=CHOICE
        )
    duedate = models.DateField()
    
    def __str__(self):
        return str(self.id) + '.' + self.title
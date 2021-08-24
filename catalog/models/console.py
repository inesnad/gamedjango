from django.db import models

class Console(models.Model):
    name = models.CharField(max_length=200, unique=True)
    def __str__(self):
    	return "default" if self.name is None else self.name
from django.db import models
from .console import Console

class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    picture = models.URLField()
    consoles = models.ManyToManyField(Console, related_name='games', blank=True)
    def __str__(self):
    	return self.title

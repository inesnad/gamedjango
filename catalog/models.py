from django.db import models


class Console(models.Model):
    name = models.CharField(max_length=200, unique=True)
    def __str__(self):
    	return self.name

class Player(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)
    def __str__(self):
    	return self.name

class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    picture = models.URLField()
    consoles = models.ManyToManyField(Console, related_name='games', blank=True)
    def __str__(self):
    	return self.title

class Result(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(null=True)
    level = models.CharField(max_length=50)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
    	if 5000 < self.score <= 10000:
        	self.level = 'Advanced'
    	elif self.score > 10000:
        	self.level = 'Expert'
    	else:
    		self.level = 'Beginner'
    	super(Result, self).save(*args, **kwargs)  # Call the "real" save() method.


    def __str__(self):
    	return str(self.score)
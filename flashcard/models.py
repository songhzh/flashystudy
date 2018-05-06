from django.db import models

# Create your models here.

class Deck(models.Model):
    deck_name = models.CharField(max_length=20)

    def __str__(self):
        return self.deck_name

class Card(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    front_text = models.CharField(max_length=100)
    back_text = models.CharField(max_length=100)

    def __str__(self):
        return self.front_text
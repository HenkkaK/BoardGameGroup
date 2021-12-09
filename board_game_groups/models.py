from django.db import models

# Create your models here.
class Game(models.Model):
  Game_name = models.CharField(max_length=300)
  
class Gamer(models.Model):
  Name = CharField(max_length=100)
  
class Loans(models.Model):
  Borrowed_Game = models.ForeignKey(Game, on_delete=models.CASCADE,)
  
  def __str__(self):
    return self.Borrower
  

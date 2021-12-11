from django.db import models

# Create your models here.

# Class for the players.
class Gamer(models.Model):
  Name = models.CharField(max_length=100)
  Owned_games = models.JSONField(default=list)
  
  def __str__(self):
    return self.Name
  
# Class for the boardgames.
class Game(models.Model):
  Game_name = models.CharField(max_length=300)
  Owner = models.CharField(max_length=30)
  Game_description = models.TextField()
  Latest_borrower =  models.ForeignKey(Gamer, on_delete=models.CASCADE,)
  is_borrowed = models.BooleanField()
  date_modified = models.DateTimeField(auto_now_add=True)
  
  
  def __str__(self):
    return self.Game_name
  
 
  
 
  

  
  """
  
class Loans(models.Model):
  Borrow_Date = models.DateTimeField(auto_now_add=True)
  Borrower = models.ForeignKey(Gamer, on_delete=models.CASCADE,)
  Borrowed_Game = models.ForeignKey(Game, on_delete=models.CASCADE,)
  
  def __str__(self):
    return self.Borrow_Date
  
"""

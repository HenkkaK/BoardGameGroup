from django.db import models

# Create your models here.

# Class for the boardgames.
class Game(models.Model):
  Game_name = models.CharField(max_length=300)
  Owner = models.CharField(max_length=30)
  Game_description = models.TextField()
  is_borrowed = models.BooleanField()
  date_added = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now_add=True)
  
  
  def __str__(self):
    return self.Game_name
  
 
  
 class Borrow(models.Model):
  Borrowed_Game = models.ForeignKey(Game, on_delete=models.CASCADE)
  Borrow_date = models.DateTimeField(auto_now_add=True)
  Planned_return_date = models.CharField(max_length=20)
  
  def __str__(self):
    return self.Borrowed_Game
  
"""
# Class for the players. (currently unused)
class Gamer(models.Model):
  Name = models.CharField(max_length=100)
  Owned_games = models.JSONField(default=list)
  Contacts = models.TextField()
  
  def __str__(self):
    return self.Name
  """
  
  

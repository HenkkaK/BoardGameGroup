from django.db import models

# Create your models here.

# Class for the boardgames.
class Game(models.Model):
  name = models.CharField(max_length=300)
  owner = models.CharField(max_length=30)
  description = models.TextField()
  is_borrowed = models.BooleanField(default=False)
  date_added = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name


class Borrow(models.Model):
  game = models.ForeignKey(Game, on_delete=models.CASCADE)
  borrow_date = models.DateTimeField(auto_now_add=True)
  contact_information = models.CharField(max_length=100)
  planned_return_date = models.CharField(max_length=20)
  
  def __str__(self):
    return self.contact_information
  
"""
# Class for the players. (currently unused)
class Gamer(models.Model):
  Name = models.CharField(max_length=100)
  Owned_games = models.JSONField(default=list)
  Contacts = models.TextField()
  
  def __str__(self):
    return self.Name
  """
  
  

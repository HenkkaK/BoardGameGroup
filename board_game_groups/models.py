from django.db import models

# Create your models here.
class Game(models.Model):
  Game_name = models.CharField(max_length=300)
  Owner = models.ForeignKey(Gamer, on_delete=models.CASCADE,)
  
  return self.Borrow_Date
  
class Gamer(models.Model):
  Name = CharField(max_length=100)
  
  
class Loans(models.Model):
  Borrow_Date = models.DateTimeField(auto_now_add=True)
  Borrower = models.ForeignKey(Gamer, on_delete=models.CASCADE,)
  Borrowed_Game = models.ForeignKey(Game, on_delete=models.CASCADE,)
  
  def __str__(self):
    return self.Borrow_Date
  

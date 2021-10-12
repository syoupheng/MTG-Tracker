from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Expansion(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    release_date = models.DateField(auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return self.name + " (" + self.code + ")"
    

class DraftResult(models.Model):
    FORMAT_CHOICES = [
        ('BO1', 'Best of one'),
        ('BO3', 'Best of three'),
    ]
    date = models.DateField(auto_now=False, auto_now_add=False)
    expansion = models.ForeignKey(Expansion, on_delete=models.CASCADE)
    best_of = models.CharField(max_length=5, choices=FORMAT_CHOICES, default='BO1')
    deck_title = models.CharField(max_length=100, null=True)
    nb_wins = models.IntegerField(validators=[MinValueValidator(0, message="Le nombre de victoires ne peut être inférieur à 0 !"),
                                                MaxValueValidator(7, message="Le nombre de victoires ne peut être supérieur à 7 !")])
    nb_losses = models.IntegerField(validators=[MinValueValidator(0, message="Le nombre de défaites ne peut être inférieur à 0 !"),
                                                MaxValueValidator(3, message="Le nombre de victoires ne peut être supérieur à 3 !")])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    colors = models.CharField(max_length=5)

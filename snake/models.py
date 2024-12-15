from django.db import models

# Create your models here.
class Jugador(models.Model):
    username = models.CharField(max_length=100)         #Registra el nombre de usuario del jugador
    score = models.IntegerField()                       #Registra el puntaje alcanzado
    game_time = models.DurationField()                  #Registra el tiempo demjuego

    def __str__(self):
        return self.username
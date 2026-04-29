from django.db import models

class Time(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    posicao = models.CharField(max_length=50)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)

class Partida(models.Model):
    time_casa = models.ForeignKey(Time, related_name='casa', on_delete=models.CASCADE)
    time_fora = models.ForeignKey(Time, related_name='fora', on_delete=models.CASCADE)
    gols_casa = models.IntegerField()
    gols_fora = models.IntegerField()
    data = models.DateField()
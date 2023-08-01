from django.db import models
from datetime import datetime

class Fotografia(models.Model):

    OPCOES = [('NEBULOSA','nebulosa'),("ESTRELA","estrela"),("GALÁXIA","galáxia"),("PLANETA","planeta"),("OUTROS",'outros')] 
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES, default='')
    descricao = models.TextField(default=False ,null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    publicada = models.BooleanField(default=False)
    

    def __str__(self):
        return self.nome


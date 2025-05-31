from django.db import models
from datetime import datetime
class Fotografia(models.Model):
    
    OPCOES_CATEGORIA = [
        ("ESTÚDIO","estudio"),
        ("AUTOMAÇÃO","automacao"),
        ("CÓDIGO","codigo"),
        ("STORYTELLING","storytelling")
    ]
    # biblioteca blue e isort
    nome = models.CharField(max_length=100,null=False,blank=False)
    legenda = models.CharField(max_length=150,null=False,blank=False)
    categoria = models.CharField(max_length=100,choices=OPCOES_CATEGORIA,default='')
    descricao = models.TextField(null=False,blank=False)
    #foto = models.CharField(max_length=100,null=False,blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/",blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now,
                                           blank=False)
    link = models.TextField(null=False,blank="False")
    tutorial = models.TextField(null=False,blank="False")
    # boa pratica
    def __str__(self):
        return f"Fotografia [nome={self.nome}] "
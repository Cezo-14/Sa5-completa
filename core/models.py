from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=50)
    data_criacao = models.DateTimeField(auto_now_add=True)
    pais = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

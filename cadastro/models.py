from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome


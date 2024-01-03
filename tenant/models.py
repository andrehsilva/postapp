from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome do grupo escolar.")
    email = models.EmailField(max_length=277, verbose_name="E-mail de contato oficial do grupo escolar.")

    def __str__(self):
        return str(self.id)
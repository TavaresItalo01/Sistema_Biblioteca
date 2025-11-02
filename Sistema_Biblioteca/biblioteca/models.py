from django.db import models

class Livro(models.Model):
    CATEGORIAS_LIVRO = [
        ('TI', 'TI'),
        ('Humanas', 'Humanas'),
        ('FiccaoRomance', 'Ficção Científica / Romance'),
        ('Saúde', 'Saúde'),
        ('Biológicas', 'Biológicas'),
        ('Exatas', 'Exatas'),
    ]

    titulo = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100, choices=CATEGORIAS_LIVRO)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'

class Autor(models.Model):
    nome = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Livro(models.Model):
    ISBN = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=250)
    publicacao = models.DateField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, related_name='livros')
    autores = models.ManyToManyField(Autor, through='Publica', related_name='livros')

    def __str__(self):
        return f"{self.titulo} ({self.ISBN})"

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

class Publica(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('livro', 'autor')
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'
        constraints = [
            models.UniqueConstraint(fields=['livro', 'autor'], name='unique_publicacao')
        ]

    def __str__(self):
        return f"{self.autor.nome} → {self.livro.titulo}"
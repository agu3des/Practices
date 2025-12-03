from django.core.management.base import BaseCommand
from faker import Faker
from catalog.models import Livro, Autor, Editora, Publica 
import random

class Command(BaseCommand):
    help = 'Gera dados fictícios para Editoras, Autores e Livros usando Faker'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Iniciando geração de dados...'))
        
        fake = Faker('pt_BR') 
        
        # 1. Gerar/Obter Editoras
        editoras = []
        for _ in range(5):
            nome = fake.company()
            # get_or_create evita erros de duplicidade (unique=True)
            editora, _ = Editora.objects.get_or_create(nome=nome)
            editoras.append(editora)
            
        # 2. Gerar/Obter Autores
        autores = []
        for _ in range(15):
            nome = fake.name()
            autor, _ = Autor.objects.get_or_create(nome=nome)
            autores.append(autor)

        # 3. Gerar Livros
        for _ in range(100):
            # Gera dados básicos
            titulo = fake.sentence(nb_words=4).replace('.', '')
            isbn = fake.isbn13()
            # Garante ISBN único
            while Livro.objects.filter(ISBN=isbn).exists():
                isbn = fake.isbn13()
                
            data_pub = fake.date_object()
            preco = round(random.uniform(20.0, 200.0), 2)
            estoque = random.randint(0, 100)
            editora_random = random.choice(editoras)

            livro = Livro.objects.create(
                titulo=titulo,
                ISBN=isbn,
                publicacao=data_pub,
                preco=preco,
                estoque=estoque,
                editora=editora_random
            )
            
            # 4. Vincular Autores (Tabela Publica)
            # Escolhe aleatoriamente 1 ou 2 autores para este livro
            autores_livro = random.sample(autores, k=random.randint(1, 2))
            for autor in autores_livro:
                Publica.objects.create(livro=livro, autor=autor)

        self.stdout.write(self.style.SUCCESS('Sucesso! 100 livros gerados com editoras e autores.'))

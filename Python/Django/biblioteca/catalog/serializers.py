from rest_framework import serializers
from .models import Autor, Editora, Livro, Publica


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nome']


class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = ['id', 'nome']


class LivroSerializer(serializers.ModelSerializer):
    editora_nome = serializers.CharField(source='editora.nome', read_only=True)
    autores = AutorSerializer(source='autores', many=True, read_only=True)

    class Meta:
        model = Livro
        fields = ['id', 'ISBN', 'titulo', 'publicacao', 'preco', 'estoque', 'editora', 'editora_nome', 'autores']


class PublicaSerializer(serializers.ModelSerializer):
    livro_titulo = serializers.CharField(source='livro.titulo', read_only=True)
    autor_nome = serializers.CharField(source='autor.nome', read_only=True)

    class Meta:
        model = Publica
        fields = ['id', 'livro', 'livro_titulo', 'autor', 'autor_nome']

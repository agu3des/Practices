# filepath: c:\Users\anand\git\Practices\Python\Django\biblioteca\catalog\admin.py
from django.contrib import admin
from .models import Editora, Autor, Livro, Publica

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'ISBN', 'titulo', 'publicacao', 'preco', 'estoque', 'editora')
    search_fields = ('titulo', 'ISBN')
    list_filter = ('editora',)

@admin.register(Publica)
class PublicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'autor', 'livro')
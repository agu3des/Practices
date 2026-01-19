from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Editora, Autor, Livro, Publica
from .forms import EditoraForm, AutorForm, LivroForm, PublicaForm
from .serializers import AutorSerializer, EditoraSerializer, LivroSerializer, PublicaSerializer

# Mixin personalizado para verificar permissão de Livro
class LivroPermissionMixin(LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = 'catalog.change_livro'
    login_url = 'admin:login'

# --- Autenticação (Sign Up) ---

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    extra_context = {'title': 'Cadastro de Utilizador'}

# --- Editora CRUD ---

class EditoraListView(generic.ListView):
    model = Editora
    template_name = 'catalog/editora_list.html'
    extra_context = {'title': 'Lista de Editoras'}

class EditoraCreateView(generic.CreateView):
    model = Editora
    form_class = EditoraForm
    template_name = 'catalog/editora_form.html'
    success_url = reverse_lazy('catalog:editora-list')
    extra_context = {
        'title': 'Nova Editora',
        'cancel_url': reverse_lazy('catalog:editora-list')
    }

class EditoraUpdateView(generic.UpdateView):
    model = Editora
    form_class = EditoraForm
    template_name = 'catalog/editora_form.html'
    success_url = reverse_lazy('catalog:editora-list')
    extra_context = {
        'title': 'Editar Editora',
        'cancel_url': reverse_lazy('catalog:editora-list')
    }

class EditoraDeleteView(generic.DeleteView):
    model = Editora
    template_name = 'catalog/editora_confirm_delete.html'
    success_url = reverse_lazy('catalog:editora-list')

# --- Autor CRUD ---

class AutorListView(generic.ListView):
    model = Autor
    template_name = 'catalog/autor_list.html'
    extra_context = {'title': 'Lista de Autores'}

class AutorCreateView(generic.CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'catalog/autor_form.html'
    success_url = reverse_lazy('catalog:autor-list')
    extra_context = {
        'title': 'Novo Autor',
        'cancel_url': reverse_lazy('catalog:autor-list')
    }

class AutorUpdateView(generic.UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'catalog/autor_form.html'
    success_url = reverse_lazy('catalog:autor-list')
    extra_context = {
        'title': 'Editar Autor',
        'cancel_url': reverse_lazy('catalog:autor-list')
    }

class AutorDeleteView(generic.DeleteView):
    model = Autor
    template_name = 'catalog/autor_confirm_delete.html'
    success_url = reverse_lazy('catalog:autor-list')

# --- Livro CRUD com Permissões ---

class LivroListView(generic.ListView):
    model = Livro
    template_name = 'catalog/livro_list.html'
    extra_context = {'title': 'Lista de Livros'}

class LivroCreateView(LivroPermissionMixin, generic.CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'catalog/livro_form.html'
    success_url = reverse_lazy('catalog:livro-list')
    permission_required = 'catalog.add_livro'
    extra_context = {
        'title': 'Novo Livro',
        'cancel_url': reverse_lazy('catalog:livro-list')
    }

    def form_valid(self, form):
        messages.success(self.request, 'Livro criado com sucesso!')
        return super().form_valid(form)

class LivroUpdateView(LivroPermissionMixin, generic.UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'catalog/livro_form.html'
    success_url = reverse_lazy('catalog:livro-list')
    permission_required = 'catalog.change_livro'
    extra_context = {
        'title': 'Editar Livro',
        'cancel_url': reverse_lazy('catalog:livro-list')
    }

    def form_valid(self, form):
        messages.success(self.request, 'Livro atualizado com sucesso!')
        return super().form_valid(form)

class LivroDeleteView(LivroPermissionMixin, generic.DeleteView):
    model = Livro
    template_name = 'catalog/livro_confirm_delete.html'
    success_url = reverse_lazy('catalog:livro-list')
    permission_required = 'catalog.delete_livro'

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Livro removido com sucesso!')
        return super().delete(request, *args, **kwargs)

# --- Publica CRUD ---

class PublicaListView(generic.ListView):
    model = Publica
    template_name = 'catalog/publica_list.html'
    extra_context = {'title': 'Lista de Publicações'}

class PublicaCreateView(generic.CreateView):
    model = Publica
    form_class = PublicaForm
    template_name = 'catalog/publica_form.html'
    success_url = reverse_lazy('catalog:publica-list')
    extra_context = {
        'title': 'Nova Publicação',
        'cancel_url': reverse_lazy('catalog:publica-list')
    }

class PublicaDeleteView(generic.DeleteView):
    model = Publica
    template_name = 'catalog/publica_confirm_delete.html'
    success_url = reverse_lazy('catalog:publica-list')


# --- API REST VIEWSETS ---

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    search_fields = ['nome']
    ordering_fields = ['id', 'nome']
    ordering = ['nome']


class EditoraViewSet(viewsets.ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    search_fields = ['nome']
    ordering_fields = ['id', 'nome']
    ordering = ['nome']


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all().select_related('editora').prefetch_related('autores')
    serializer_class = LivroSerializer
    search_fields = ['titulo', 'ISBN']
    ordering_fields = ['id', 'titulo', 'publicacao', 'preco']
    ordering = ['-publicacao']


class PublicaViewSet(viewsets.ModelViewSet):
    queryset = Publica.objects.all().select_related('livro', 'autor')
    serializer_class = PublicaSerializer
    search_fields = ['livro__titulo', 'autor__nome']
    ordering_fields = ['id', 'livro__titulo', 'autor__nome']
    ordering = ['livro__titulo']

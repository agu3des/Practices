from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Editora, Autor, Livro, Publica
from .forms import EditoraForm, AutorForm, LivroForm, PublicaForm

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

class EditoraCreateView(LoginRequiredMixin, generic.CreateView):
    model = Editora
    form_class = EditoraForm
    template_name = 'catalog/editora_form.html'
    success_url = reverse_lazy('catalog:editora-list')
    extra_context = {
        'title': 'Nova Editora',
        'cancel_url': reverse_lazy('catalog:editora-list')
    }

class EditoraUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Editora
    form_class = EditoraForm
    template_name = 'catalog/editora_form.html'
    success_url = reverse_lazy('catalog:editora-list')
    extra_context = {
        'title': 'Editar Editora',
        'cancel_url': reverse_lazy('catalog:editora-list')
    }

class EditoraDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Editora
    template_name = 'catalog/editora_confirm_delete.html'
    success_url = reverse_lazy('catalog:editora-list')
    extra_context = {
        'title': 'Excluir Editora',
        'cancel_url': reverse_lazy('catalog:editora-list')
    }

# --- Autor CRUD ---

class AutorListView(generic.ListView):
    model = Autor
    template_name = 'catalog/autor_list.html'
    extra_context = {'title': 'Lista de Autores'}

class AutorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'catalog/autor_form.html'
    success_url = reverse_lazy('catalog:autor-list')
    extra_context = {
        'title': 'Novo Autor',
        'cancel_url': reverse_lazy('catalog:autor-list')
    }

class AutorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'catalog/autor_form.html'
    success_url = reverse_lazy('catalog:autor-list')
    extra_context = {
        'title': 'Editar Autor',
        'cancel_url': reverse_lazy('catalog:autor-list')
    }

class AutorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Autor
    template_name = 'catalog/autor_confirm_delete.html'
    success_url = reverse_lazy('catalog:autor-list')
    extra_context = {
        'title': 'Excluir Autor',
        'cancel_url': reverse_lazy('catalog:autor-list')
    }

# --- Livro CRUD ---

class LivroListView(generic.ListView):
    model = Livro
    template_name = 'catalog/livro_list.html'
    extra_context = {'title': 'Lista de Livros'}
    paginate_by = 10 

    def get_queryset(self):
        # Otimização para evitar N+1 queries
        return Livro.objects.all().select_related('editora').prefetch_related('autores').order_by('-id')

class LivroCreateView(LoginRequiredMixin, generic.CreateView):
    model = Livro
    # Usamos fields explícitos para evitar erro com o M2M 'through'
    fields = ['ISBN', 'titulo', 'publicacao', 'preco', 'estoque', 'editora']
    template_name = 'catalog/livro_form.html'
    success_url = reverse_lazy('catalog:livro-list')
    extra_context = {
        'title': 'Novo Livro',
        'cancel_url': reverse_lazy('catalog:livro-list')
    }

class LivroUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Livro
    fields = ['ISBN', 'titulo', 'publicacao', 'preco', 'estoque', 'editora']
    template_name = 'catalog/livro_form.html'
    success_url = reverse_lazy('catalog:livro-list')
    extra_context = {
        'title': 'Editar Livro',
        'cancel_url': reverse_lazy('catalog:livro-list')
    }

class LivroDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Livro
    template_name = 'catalog/livro_confirm_delete.html'
    success_url = reverse_lazy('catalog:livro-list')
    extra_context = {
        'title': 'Excluir Livro',
        'cancel_url': reverse_lazy('catalog:livro-list')
    }

# --- Publica CRUD ---

class PublicaListView(generic.ListView):
    model = Publica
    template_name = 'catalog/publica_list.html'
    extra_context = {'title': 'Lista de Publicações'}

class PublicaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Publica
    form_class = PublicaForm
    template_name = 'catalog/publica_form.html'
    success_url = reverse_lazy('catalog:publica-list')
    extra_context = {
        'title': 'Nova Publicação',
        'cancel_url': reverse_lazy('catalog:publica-list')
    }

class PublicaDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Publica
    template_name = 'catalog/publica_confirm_delete.html'
    success_url = reverse_lazy('catalog:publica-list')
    extra_context = {
        'title': 'Excluir Publicação',
        'cancel_url': reverse_lazy('catalog:publica-list')
    }
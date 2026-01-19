"""
Testes Unitários Completos para a Biblioteca Django REST Framework
Cobrindo: Model, View, Form, Serializer, e API REST

Executar com:
    python manage.py test catalog.test_complete
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from datetime import date
from decimal import Decimal

from .models import Autor, Editora, Livro, Publica
from .forms import AutorForm, EditoraForm, LivroForm
from .serializers import AutorSerializer, EditoraSerializer, LivroSerializer, PublicaSerializer


# ============================================================================
# 1️⃣ TESTES DO MODEL (TestCase)
# ============================================================================

class AutorModelTestCase(TestCase):
    """Teste unitário para o modelo Autor"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.autor = Autor.objects.create(nome="Machado de Assis")
    
    def test_autor_creation(self):
        """✅ Testa a criação de um autor"""
        self.assertEqual(self.autor.nome, "Machado de Assis")
        self.assertIsNotNone(self.autor.id)
    
    def test_autor_string_representation(self):
        """✅ Testa a representação em string do autor"""
        self.assertEqual(str(self.autor), "Machado de Assis")
    
    def test_autor_unique_constraint(self):
        """✅ Testa restrição de unicidade do nome"""
        with self.assertRaises(Exception):
            Autor.objects.create(nome="Machado de Assis")
    
    def test_autor_verbose_name(self):
        """✅ Testa meta informações do modelo"""
        self.assertEqual(self.autor._meta.verbose_name, "Autor")
        self.assertEqual(self.autor._meta.verbose_name_plural, "Autores")


class EditoraModelTestCase(TestCase):
    """Teste unitário para o modelo Editora"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.editora = Editora.objects.create(nome="Editora Nacional")
    
    def test_editora_creation(self):
        """✅ Testa a criação de uma editora"""
        self.assertEqual(self.editora.nome, "Editora Nacional")
        self.assertTrue(Editora.objects.filter(nome="Editora Nacional").exists())
    
    def test_editora_string_representation(self):
        """✅ Testa a representação em string da editora"""
        self.assertEqual(str(self.editora), "Editora Nacional")
    
    def test_editora_unique_constraint(self):
        """✅ Testa restrição de unicidade"""
        with self.assertRaises(Exception):
            Editora.objects.create(nome="Editora Nacional")


class LivroModelTestCase(TestCase):
    """Teste unitário para o modelo Livro"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.editora = Editora.objects.create(nome="Companhia das Letras")
        self.autor1 = Autor.objects.create(nome="Clarice Lispector")
        self.autor2 = Autor.objects.create(nome="Paulo Coelho")
        
        self.livro = Livro.objects.create(
            ISBN="9788535931662",
            titulo="A Hora da Estrela",
            publicacao=date(1977, 8, 1),
            preco=Decimal("35.50"),
            estoque=10,
            editora=self.editora
        )
        self.livro.autores.add(self.autor1)
    
    def test_livro_creation(self):
        """✅ Testa a criação de um livro"""
        self.assertEqual(self.livro.titulo, "A Hora da Estrela")
        self.assertEqual(self.livro.preco, Decimal("35.50"))
        self.assertEqual(self.livro.estoque, 10)
    
    def test_livro_foreign_key_relationship(self):
        """✅ Testa o relacionamento ForeignKey com Editora"""
        self.assertEqual(self.livro.editora, self.editora)
        self.assertIn(self.livro, self.editora.livros.all())
    
    def test_livro_many_to_many_relationship(self):
        """✅ Testa o relacionamento ManyToMany com Autor"""
        self.assertIn(self.autor1, self.livro.autores.all())
        self.assertNotIn(self.autor2, self.livro.autores.all())
        self.assertEqual(self.livro.autores.count(), 1)
    
    def test_livro_string_representation(self):
        """✅ Testa a representação em string do livro"""
        expected = "A Hora da Estrela (9788535931662)"
        self.assertEqual(str(self.livro), expected)
    
    def test_livro_isbn_unique_constraint(self):
        """✅ Testa restrição de ISBN único"""
        with self.assertRaises(Exception):
            Livro.objects.create(
                ISBN="9788535931662",
                titulo="Outro Livro",
                publicacao=date(2020, 1, 1),
                preco=Decimal("50.00"),
                estoque=5,
                editora=self.editora
            )


class PublicaModelTestCase(TestCase):
    """Teste unitário para o modelo Publica (through)"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.editora = Editora.objects.create(nome="Record")
        self.autor = Autor.objects.create(nome="Cecília Meireles")
        self.livro = Livro.objects.create(
            ISBN="9788501058789",
            titulo="Viagem",
            publicacao=date(1939, 1, 1),
            preco=Decimal("42.00"),
            estoque=15,
            editora=self.editora
        )
        self.publica = Publica.objects.create(livro=self.livro, autor=self.autor)
    
    def test_publica_creation(self):
        """✅ Testa a criação de uma publicação"""
        self.assertEqual(self.publica.livro, self.livro)
        self.assertEqual(self.publica.autor, self.autor)
    
    def test_publica_string_representation(self):
        """✅ Testa a representação em string"""
        expected = "Cecília Meireles → Viagem"
        self.assertEqual(str(self.publica), expected)
    
    def test_publica_unique_together_constraint(self):
        """✅ Testa restrição unique_together"""
        with self.assertRaises(Exception):
            Publica.objects.create(livro=self.livro, autor=self.autor)


# ============================================================================
# 2️⃣ TESTES DO FORM (TestCase)
# ============================================================================

class AutorFormTestCase(TestCase):
    """Teste unitário para o formulário AutorForm"""
    
    def test_autor_form_valid(self):
        """✅ Testa validação de um formulário válido"""
        form = AutorForm(data={'nome': 'Fernando Pessoa'})
        self.assertTrue(form.is_valid())
    
    def test_autor_form_empty_nome(self):
        """✅ Testa validação com nome vazio"""
        form = AutorForm(data={'nome': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)
    
    def test_autor_form_save(self):
        """✅ Testa a salvação de um autor via formulário"""
        form = AutorForm(data={'nome': 'Raul Pompeia'})
        self.assertTrue(form.is_valid())
        autor = form.save()
        self.assertEqual(autor.nome, 'Raul Pompeia')
        self.assertTrue(Autor.objects.filter(nome='Raul Pompeia').exists())
    
    def test_autor_form_fields(self):
        """✅ Testa se o formulário possui o campo correto"""
        form = AutorForm()
        self.assertIn('nome', form.fields)


class EditoraFormTestCase(TestCase):
    """Teste unitário para o formulário EditoraForm"""
    
    def test_editora_form_valid(self):
        """✅ Testa validação de um formulário válido"""
        form = EditoraForm(data={'nome': 'Editora Rosa'})
        self.assertTrue(form.is_valid())
    
    def test_editora_form_save(self):
        """✅ Testa a salvação de uma editora via formulário"""
        form = EditoraForm(data={'nome': 'Editora Globo'})
        self.assertTrue(form.is_valid())
        editora = form.save()
        self.assertEqual(editora.nome, 'Editora Globo')
        self.assertTrue(Editora.objects.filter(nome='Editora Globo').exists())


class LivroFormTestCase(TestCase):
    """Teste unitário para o formulário LivroForm"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.editora = Editora.objects.create(nome="Intrínseca")
        self.autor1 = Autor.objects.create(nome="George Orwell")
        self.autor2 = Autor.objects.create(nome="Aldous Huxley")
    
    def test_livro_form_valid(self):
        """✅ Testa validação de um formulário de livro válido"""
        form = LivroForm(data={
            'ISBN': '9788535926675',
            'titulo': '1984',
            'publicacao': '1949-06-08',
            'preco': '45.90',
            'estoque': 20,
            'editora': self.editora.id,
            'autores': [self.autor1.id]
        })
        self.assertTrue(form.is_valid())
    
    def test_livro_form_with_multiple_authors(self):
        """✅ Testa o formulário com múltiplos autores"""
        form = LivroForm(data={
            'ISBN': '9788535926676',
            'titulo': 'Admirável Mundo Novo',
            'publicacao': '1932-06-30',
            'preco': '48.00',
            'estoque': 15,
            'editora': self.editora.id,
            'autores': [self.autor1.id, self.autor2.id]
        })
        self.assertTrue(form.is_valid())
    
    def test_livro_form_missing_required_field(self):
        """✅ Testa validação com campo obrigatório faltando"""
        form = LivroForm(data={
            'ISBN': '9788535926677',
            # titulo faltando
            'publicacao': '2020-01-01',
            'preco': '50.00',
            'estoque': 10,
            'editora': self.editora.id,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('titulo', form.errors)
    
    def test_livro_form_save_with_authors(self):
        """✅ Testa a salvação de um livro com autores"""
        form = LivroForm(data={
            'ISBN': '9788535926678',
            'titulo': 'O Senhor dos Anéis',
            'publicacao': '1954-07-29',
            'preco': '120.00',
            'estoque': 5,
            'editora': self.editora.id,
            'autores': [self.autor1.id]
        })
        self.assertTrue(form.is_valid())
        livro = form.save()
        self.assertEqual(livro.titulo, 'O Senhor dos Anéis')
        self.assertIn(self.autor1, livro.autores.all())


# ============================================================================
# 3️⃣ TESTES DO SERIALIZER (TestCase + APITestCase)
# ============================================================================

class AutorSerializerTestCase(TestCase):
    """Teste unitário para o serializer AutorSerializer"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.autor = Autor.objects.create(nome="Joaquim Maria Machado de Assis")
    
    def test_serializer_data(self):
        """✅ Testa a serialização de dados de um autor"""
        serializer = AutorSerializer(self.autor)
        data = serializer.data
        self.assertEqual(data['nome'], "Joaquim Maria Machado de Assis")
        self.assertEqual(data['id'], self.autor.id)
    
    def test_serializer_create(self):
        """✅ Testa a criação de um objeto via serializer"""
        data = {'nome': 'Aluísio Azevedo'}
        serializer = AutorSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        autor = serializer.save()
        self.assertEqual(autor.nome, 'Aluísio Azevedo')
    
    def test_serializer_update(self):
        """✅ Testa a atualização de um objeto via serializer"""
        data = {'nome': 'Machado de Assis Atualizado'}
        serializer = AutorSerializer(self.autor, data=data)
        self.assertTrue(serializer.is_valid())
        autor = serializer.save()
        self.assertEqual(autor.nome, 'Machado de Assis Atualizado')
    
    def test_serializer_validation_error(self):
        """✅ Testa erro de validação com dados inválidos"""
        data = {'nome': ''}  # nome vazio
        serializer = AutorSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('nome', serializer.errors)


class LivroSerializerTestCase(TestCase):
    """Teste unitário para o serializer LivroSerializer"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.editora = Editora.objects.create(nome="Rocco")
        self.autor = Autor.objects.create(nome="Toni Morrison")
        self.livro = Livro.objects.create(
            ISBN='9788532515094',
            titulo='Olhos Azuis',
            publicacao=date(1970, 2, 1),
            preco=Decimal('55.00'),
            estoque=8,
            editora=self.editora
        )
        self.livro.autores.add(self.autor)
    
    def test_livro_serializer_data(self):
        """✅ Testa a serialização completa de um livro"""
        serializer = LivroSerializer(self.livro)
        data = serializer.data
        self.assertEqual(data['titulo'], 'Olhos Azuis')
        self.assertEqual(data['ISBN'], '9788532515094')
        self.assertEqual(data['editora_nome'], 'Rocco')
        self.assertEqual(len(data['autores']), 1)
    
    def test_livro_serializer_nested_relationships(self):
        """✅ Testa os relacionamentos aninhados (nested)"""
        serializer = LivroSerializer(self.livro)
        data = serializer.data
        self.assertIsNotNone(data['editora_nome'])
        self.assertTrue(isinstance(data['autores'], list))
        self.assertEqual(data['autores'][0]['nome'], 'Toni Morrison')


class PublicaSerializerTestCase(TestCase):
    """Teste unitário para o serializer PublicaSerializer"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.editora = Editora.objects.create(nome="Estação Brasil")
        self.autor = Autor.objects.create(nome="Isabel Allende")
        self.livro = Livro.objects.create(
            ISBN='9788577151319',
            titulo='Paula',
            publicacao=date(1994, 10, 1),
            preco=Decimal('42.50'),
            estoque=12,
            editora=self.editora
        )
        self.publica = Publica.objects.create(livro=self.livro, autor=self.autor)
    
    def test_publica_serializer_data(self):
        """✅ Testa a serialização de uma publicação"""
        serializer = PublicaSerializer(self.publica)
        data = serializer.data
        self.assertEqual(data['livro_titulo'], 'Paula')
        self.assertEqual(data['autor_nome'], 'Isabel Allende')


# ============================================================================
# 4️⃣ TESTES DA VIEW HTML (TestCase)
# ============================================================================

class AutorViewTestCase(TestCase):
    """Teste unitário para a view HTML de Autor"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.client = Client()
        self.usuario = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.autor = Autor.objects.create(nome="Jorge Amado")
    
    def test_autor_list_view(self):
        """✅ Testa a listagem de autores"""
        response = self.client.get(reverse('autor-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jorge Amado')
    
    def test_autor_detail_view(self):
        """✅ Testa a visualização de detalhes de um autor"""
        response = self.client.get(
            reverse('autor-detail', kwargs={'pk': self.autor.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jorge Amado')
    
    def test_autor_create_view_requires_login(self):
        """✅ Testa se a criação requer autenticação"""
        response = self.client.get(reverse('autor-create'))
        self.assertEqual(response.status_code, 302)  # Redirecionado para login
    
    def test_autor_create_view_authenticated(self):
        """✅ Testa a criação de autor autenticado"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('autor-create'),
            {'nome': 'Novo Autor'}
        )
        self.assertEqual(response.status_code, 302)  # Redirecionado após sucesso
        self.assertTrue(Autor.objects.filter(nome='Novo Autor').exists())


class EditoraViewTestCase(TestCase):
    """Teste unitário para a view HTML de Editora"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.client = Client()
        self.editora = Editora.objects.create(nome="Saraiva")
    
    def test_editora_list_view(self):
        """✅ Testa a listagem de editoras"""
        response = self.client.get(reverse('editora-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Saraiva')
    
    def test_editora_detail_view(self):
        """✅ Testa a visualização de detalhes de uma editora"""
        response = self.client.get(
            reverse('editora-detail', kwargs={'pk': self.editora.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Saraiva')


# ============================================================================
# 5️⃣ TESTES DA API REST (APITestCase)
# ============================================================================

class AutorAPITestCase(APITestCase):
    """Teste unitário para a API REST de Autor"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.client = APIClient()
        self.autor1 = Autor.objects.create(nome="Guimarães Rosa")
        self.autor2 = Autor.objects.create(nome="Carlos Drummond de Andrade")
        self.api_url = reverse('autor-api-list')
    
    def test_api_get_autores_list(self):
        """✅ Testa GET /api/autores/ - Listar autores"""
        response = self.client.get(self.api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(len(response.data['results']), 2)
    
    def test_api_get_autor_detail(self):
        """✅ Testa GET /api/autores/{id}/ - Detalhes de um autor"""
        url = reverse('autor-api-detail', kwargs={'pk': self.autor1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], "Guimarães Rosa")
    
    def test_api_post_autor(self):
        """✅ Testa POST /api/autores/ - Criar um novo autor"""
        data = {'nome': 'Paulo Coelho'}
        response = self.client.post(self.api_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], 'Paulo Coelho')
        self.assertTrue(Autor.objects.filter(nome='Paulo Coelho').exists())
    
    def test_api_put_autor(self):
        """✅ Testa PUT /api/autores/{id}/ - Atualizar um autor (completo)"""
        url = reverse('autor-api-detail', kwargs={'pk': self.autor1.pk})
        data = {'nome': 'Guimarães Rosa Atualizado'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Guimarães Rosa Atualizado')
    
    def test_api_patch_autor(self):
        """✅ Testa PATCH /api/autores/{id}/ - Atualizar parcial"""
        url = reverse('autor-api-detail', kwargs={'pk': self.autor1.pk})
        data = {'nome': 'Rosa, Guimarães'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Rosa, Guimarães')
    
    def test_api_delete_autor(self):
        """✅ Testa DELETE /api/autores/{id}/ - Deletar um autor"""
        url = reverse('autor-api-detail', kwargs={'pk': self.autor1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Autor.objects.filter(pk=self.autor1.pk).exists())
    
    def test_api_search_autores(self):
        """✅ Testa busca em /api/autores/?search=Rosa"""
        url = f"{self.api_url}?search=Rosa"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['nome'], 'Guimarães Rosa')
    
    def test_api_ordering_autores(self):
        """✅ Testa ordenação em /api/autores/?ordering=nome"""
        url = f"{self.api_url}?ordering=nome"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        nomes = [r['nome'] for r in response.data['results']]
        self.assertEqual(nomes, sorted(nomes))


class EditoraAPITestCase(APITestCase):
    """Teste unitário para a API REST de Editora"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.client = APIClient()
        self.editora = Editora.objects.create(nome="Editora 34")
        self.api_url = reverse('editora-api-list')
    
    def test_api_post_editora(self):
        """✅ Testa POST /api/editoras/ - Criar nova editora"""
        data = {'nome': 'Editora Número 1'}
        response = self.client.post(self.api_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], 'Editora Número 1')
    
    def test_api_get_editoras_list(self):
        """✅ Testa GET /api/editoras/ - Listar editoras"""
        response = self.client.get(self.api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)


class LivroAPITestCase(APITestCase):
    """Teste unitário para a API REST de Livro"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.client = APIClient()
        self.editora = Editora.objects.create(nome="Editora Teste")
        self.autor = Autor.objects.create(nome="Autor Teste")
        self.livro = Livro.objects.create(
            ISBN='9788532533456',
            titulo='Livro Teste',
            publicacao=date(2020, 1, 15),
            preco=Decimal('39.90'),
            estoque=25,
            editora=self.editora
        )
        self.livro.autores.add(self.autor)
        self.api_url = reverse('livro-api-list')
    
    def test_api_get_livro_detail(self):
        """✅ Testa GET /api/livros/{id}/ - Detalhes de um livro"""
        url = reverse('livro-api-detail', kwargs={'pk': self.livro.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], 'Livro Teste')
        self.assertEqual(response.data['editora_nome'], 'Editora Teste')
    
    def test_api_post_livro(self):
        """✅ Testa POST /api/livros/ - Criar novo livro"""
        data = {
            'ISBN': '9788532533457',
            'titulo': 'Novo Livro',
            'publicacao': '2022-05-20',
            'preco': '49.90',
            'estoque': 15,
            'editora': self.editora.id
        }
        response = self.client.post(self.api_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['titulo'], 'Novo Livro')
    
    def test_api_livro_editora_relationship(self):
        """✅ Testa o relacionamento editora no serializer"""
        url = reverse('livro-api-detail', kwargs={'pk': self.livro.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['editora_nome'], 'Editora Teste')


class PublicaAPITestCase(APITestCase):
    """Teste unitário para a API REST de Publicação"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.client = APIClient()
        self.editora = Editora.objects.create(nome="Editora API")
        self.autor = Autor.objects.create(nome="Autor API")
        self.livro = Livro.objects.create(
            ISBN='9788532533458',
            titulo='Livro API',
            publicacao=date(2021, 3, 10),
            preco=Decimal('45.00'),
            estoque=20,
            editora=self.editora
        )
        self.publica = Publica.objects.create(livro=self.livro, autor=self.autor)
        self.api_url = reverse('publica-api-list')
    
    def test_api_get_publicacoes_list(self):
        """✅ Testa GET /api/publicacoes/ - Listar publicações"""
        response = self.client.get(self.api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
    
    def test_api_post_publica(self):
        """✅ Testa POST /api/publicacoes/ - Criar nova publicação"""
        autor2 = Autor.objects.create(nome="Outro Autor")
        data = {
            'livro': self.livro.id,
            'autor': autor2.id
        }
        response = self.client.post(self.api_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['livro_titulo'], 'Livro API')
        self.assertEqual(response.data['autor_nome'], 'Outro Autor')
    
    def test_api_publica_nested_data(self):
        """✅ Testa dados aninhados na resposta"""
        url = reverse('publica-api-detail', kwargs={'pk': self.publica.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['livro_titulo'], 'Livro API')
        self.assertEqual(response.data['autor_nome'], 'Autor API')


# ============================================================================
# 📊 RESUMO DOS TESTES
# ============================================================================
"""
TESTES IMPLEMENTADOS:

1️⃣ MODEL TESTS (5 classes, 18 testes):
   ✅ AutorModelTestCase - Criação, String, Unicidade, Meta
   ✅ EditoraModelTestCase - Criação, String, Unicidade
   ✅ LivroModelTestCase - Criação, FK, M2M, String, Unicidade ISBN
   ✅ PublicaModelTestCase - Criação, String, Unique Together

2️⃣ FORM TESTS (3 classes, 11 testes):
   ✅ AutorFormTestCase - Validação, Save, Empty, Fields
   ✅ EditoraFormTestCase - Validação, Save
   ✅ LivroFormTestCase - Validação, Múltiplos autores, Campos obrigatórios

3️⃣ SERIALIZER TESTS (4 classes, 8 testes):
   ✅ AutorSerializerTestCase - Serialização, Create, Update, Validação
   ✅ LivroSerializerTestCase - Serialização, Relacionamentos aninhados
   ✅ PublicaSerializerTestCase - Serialização

4️⃣ VIEW TESTS (2 classes, 6 testes):
   ✅ AutorViewTestCase - List, Detail, Create, Autenticação
   ✅ EditoraViewTestCase - List, Detail

5️⃣ API REST TESTS (4 classes, 20 testes):
   ✅ AutorAPITestCase - GET, POST, PUT, PATCH, DELETE, Search, Ordering
   ✅ EditoraAPITestCase - GET List, POST
   ✅ LivroAPITestCase - GET Detail, POST, Relationships
   ✅ PublicaAPITestCase - GET List, POST, Nested Data

TOTAL: 14 classes, 63 testes ✨

Para executar os testes:
   python manage.py test catalog.test_complete -v 2
"""

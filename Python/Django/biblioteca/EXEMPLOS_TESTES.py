"""
📖 Exemplos Práticos: Como Usar e Escrever Testes Unitários
Demonstrações de como executar e estender os testes existentes
"""

# ============================================================================
# 🚀 COMO EXECUTAR OS TESTES (Linha de Comando)
# ============================================================================

"""
EXEMPLO 1: Executar todos os 63 testes
---
cd c:\Users\anand\git\Practices\Python\Django\biblioteca
python manage.py test catalog.test_complete -v 2

SAÍDA ESPERADA:
test_autor_creation (catalog.test_complete.AutorModelTestCase) ... ok
test_autor_string_representation (catalog.test_complete.AutorModelTestCase) ... ok
...
Ran 63 tests in 2.345s
OK ✅


EXEMPLO 2: Executar apenas testes de Model
---
python manage.py test catalog.test_complete.AutorModelTestCase -v 2
python manage.py test catalog.test_complete.EditoraModelTestCase -v 2
python manage.py test catalog.test_complete.LivroModelTestCase -v 2

RESULTADO:
Ran 4 tests in 0.123s
OK ✅


EXEMPLO 3: Executar apenas testes da API
---
python manage.py test catalog.test_complete.AutorAPITestCase -v 2

RESULTADO:
Ran 8 tests in 0.456s
OK ✅


EXEMPLO 4: Executar teste específico
---
python manage.py test catalog.test_complete.AutorModelTestCase.test_autor_creation

RESULTADO:
test_autor_creation ... ok
Ran 1 test in 0.012s
OK ✅


EXEMPLO 5: Executar com verbosidade baixa (resumido)
---
python manage.py test catalog.test_complete

SAÍDA RESUMIDA:
......................................................
Ran 63 tests in 2.345s
OK


EXEMPLO 6: Medir cobertura de testes
---
coverage run --source='catalog' manage.py test catalog.test_complete
coverage report -m
coverage html

RESULTADO:
Name                          Stmts   Miss  Cover
catalog/models.py                45      2    95%
catalog/forms.py                 30      1    97%
catalog/views.py                 80      5    93%
catalog/serializers.py           50      2    96%
---

EXEMPLO 7: Usar o script PowerShell
---
.\run_tests.ps1 -Type All
.\run_tests.ps1 -Type Model
.\run_tests.ps1 -Type API
.\run_tests.ps1 -Type Coverage
.\run_tests.ps1 -Type Specific -TestName "AutorAPITestCase.test_api_post_autor"
"""


# ============================================================================
# 📝 EXEMPLO 1: TEST CASE - Testando um Model
# ============================================================================

from django.test import TestCase
from catalog.models import Autor

class AutorModelExemplo(TestCase):
    """
    Exemplo: Como escrever um teste para um modelo Django
    """
    
    def setUp(self):
        """
        setUp() é chamado ANTES de cada teste
        Use para criar dados de teste reutilizáveis
        """
        # Criar dados de teste
        self.autor = Autor.objects.create(nome="Fernando Pessoa")
    
    def test_criar_autor(self):
        """
        Teste: Verificar se um Autor é criado corretamente
        """
        # ARRANGE (Preparar) - Já feito em setUp()
        
        # ACT (Agir)
        autor = Autor.objects.get(nome="Fernando Pessoa")
        
        # ASSERT (Verificar)
        self.assertEqual(autor.nome, "Fernando Pessoa")
        self.assertIsNotNone(autor.id)
        self.assertTrue(Autor.objects.filter(nome="Fernando Pessoa").exists())
    
    def test_string_representation(self):
        """
        Teste: Verificar se __str__() retorna o correto
        """
        resultado = str(self.autor)
        self.assertEqual(resultado, "Fernando Pessoa")
    
    def test_rejeitar_duplicado(self):
        """
        Teste: Verificar se a constraint UNIQUE funciona
        """
        from django.db import IntegrityError
        
        with self.assertRaises(IntegrityError):
            Autor.objects.create(nome="Fernando Pessoa")


# ============================================================================
# 📝 EXEMPLO 2: TEST CASE - Testando um Formulário
# ============================================================================

from django.test import TestCase
from catalog.forms import AutorForm

class AutorFormExemplo(TestCase):
    """
    Exemplo: Como escrever um teste para um formulário Django
    """
    
    def test_formulario_valido(self):
        """
        Teste: Form com dados válidos deve ser válido
        """
        # ARRANGE - Dados válidos
        dados = {'nome': 'Oscar Wilde'}
        
        # ACT - Criar formulário
        formulario = AutorForm(data=dados)
        
        # ASSERT - Verificar
        self.assertTrue(formulario.is_valid())
    
    def test_formulario_invalido(self):
        """
        Teste: Form com dados ausentes deve ser inválido
        """
        # ARRANGE - Dados inválidos (nome vazio)
        dados = {'nome': ''}
        
        # ACT
        formulario = AutorForm(data=dados)
        
        # ASSERT
        self.assertFalse(formulario.is_valid())
        self.assertIn('nome', formulario.errors)
        self.assertEqual(
            formulario.errors['nome'][0],
            'Este campo é obrigatório.'
        )
    
    def test_salvar_formulario(self):
        """
        Teste: Form deve salvar dados no banco
        """
        # ARRANGE
        dados = {'nome': 'William Shakespeare'}
        formulario = AutorForm(data=dados)
        
        # ACT
        self.assertTrue(formulario.is_valid())
        autor = formulario.save()
        
        # ASSERT
        self.assertEqual(autor.nome, 'William Shakespeare')
        self.assertIsNotNone(autor.id)
        self.assertTrue(
            Autor.objects.filter(nome='William Shakespeare').exists()
        )


# ============================================================================
# 📝 EXEMPLO 3: TEST CASE - Testando um Serializer
# ============================================================================

from rest_framework.test import APITestCase
from catalog.serializers import AutorSerializer
from catalog.models import Autor

class AutorSerializerExemplo(APITestCase):
    """
    Exemplo: Como escrever um teste para um DRF Serializer
    """
    
    def test_serializar_objeto(self):
        """
        Teste: Serializer converte modelo em JSON/dict
        """
        # ARRANGE - Criar modelo
        autor = Autor.objects.create(nome="Jane Austen")
        
        # ACT - Serializar
        serializer = AutorSerializer(autor)
        
        # ASSERT - Verificar dados
        dados = serializer.data
        self.assertEqual(dados['nome'], 'Jane Austen')
        self.assertEqual(dados['id'], autor.id)
    
    def test_criar_via_serializer(self):
        """
        Teste: Serializer pode criar novo objeto via POST
        """
        # ARRANGE - Dados de entrada
        dados = {'nome': 'Agatha Christie'}
        
        # ACT - Criar serializer com dados
        serializer = AutorSerializer(data=dados)
        
        # ASSERT
        self.assertTrue(serializer.is_valid())
        autor = serializer.save()
        self.assertEqual(autor.nome, 'Agatha Christie')
        self.assertTrue(Autor.objects.filter(nome='Agatha Christie').exists())
    
    def test_atualizar_via_serializer(self):
        """
        Teste: Serializer pode atualizar objeto via PUT/PATCH
        """
        # ARRANGE
        autor = Autor.objects.create(nome="Stephen King")
        dados = {'nome': 'Stephen Edwin King'}
        
        # ACT
        serializer = AutorSerializer(autor, data=dados)
        
        # ASSERT
        self.assertTrue(serializer.is_valid())
        autor_atualizado = serializer.save()
        self.assertEqual(autor_atualizado.nome, 'Stephen Edwin King')
    
    def test_validacao_serializer(self):
        """
        Teste: Serializer rejeita dados inválidos
        """
        # ARRANGE
        dados = {'nome': ''}  # Nome vazio
        
        # ACT
        serializer = AutorSerializer(data=dados)
        
        # ASSERT
        self.assertFalse(serializer.is_valid())
        self.assertIn('nome', serializer.errors)


# ============================================================================
# 📝 EXEMPLO 4: TEST CASE - Testando Views HTML
# ============================================================================

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from catalog.models import Autor

class AutorViewExemplo(TestCase):
    """
    Exemplo: Como escrever um teste para views HTML (sem API)
    """
    
    def setUp(self):
        """Preparação para cada teste"""
        self.client = Client()
        self.usuario = User.objects.create_user(
            username='testuser',
            password='senha123'
        )
        self.autor = Autor.objects.create(nome="Ray Bradbury")
    
    def test_listar_autores(self):
        """
        Teste: GET /autores/ retorna lista com 200 OK
        """
        # ACT
        response = self.client.get(reverse('autor-list'))
        
        # ASSERT
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ray Bradbury')
        self.assertTemplateUsed(response, 'catalog/autor_list.html')
    
    def test_detalhe_autor(self):
        """
        Teste: GET /autores/{id}/ retorna detalhes
        """
        # ACT
        response = self.client.get(
            reverse('autor-detail', kwargs={'pk': self.autor.pk})
        )
        
        # ASSERT
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ray Bradbury')
    
    def test_criar_autor_requer_login(self):
        """
        Teste: GET /autores/create/ sem login redireciona
        """
        # ACT
        response = self.client.get(reverse('autor-create'))
        
        # ASSERT
        self.assertEqual(response.status_code, 302)  # Redirecionado
        self.assertIn('/accounts/login/', response.url)
    
    def test_criar_autor_autenticado(self):
        """
        Teste: Usuário autenticado pode criar autor
        """
        # ARRANGE
        self.client.login(username='testuser', password='senha123')
        
        # ACT
        response = self.client.post(
            reverse('autor-create'),
            {'nome': 'Isaac Asimov'}
        )
        
        # ASSERT
        self.assertEqual(response.status_code, 302)  # Redirecionado após sucesso
        self.assertTrue(Autor.objects.filter(nome='Isaac Asimov').exists())


# ============================================================================
# 📝 EXEMPLO 5: TEST CASE - Testando API REST
# ============================================================================

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from catalog.models import Autor

class AutorAPIExemplo(APITestCase):
    """
    Exemplo: Como escrever testes para API REST com DRF
    """
    
    def setUp(self):
        """Preparação para cada teste"""
        self.client = APIClient()
        self.autor1 = Autor.objects.create(nome="Philip K. Dick")
        self.autor2 = Autor.objects.create(nome="Arthur C. Clarke")
    
    def test_listar_autores(self):
        """
        Teste: GET /api/autores/ retorna JSON com paginação
        """
        # ACT
        response = self.client.get(reverse('autor-api-list'))
        
        # ASSERT
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(len(response.data['results']), 2)
        # Verificar estrutura
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        self.assertIn('results', response.data)
    
    def test_obter_detalhe_autor(self):
        """
        Teste: GET /api/autores/{id}/ retorna JSON específico
        """
        # ACT
        url = reverse('autor-api-detail', kwargs={'pk': self.autor1.pk})
        response = self.client.get(url)
        
        # ASSERT
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], "Philip K. Dick")
        self.assertEqual(response.data['id'], self.autor1.pk)
    
    def test_criar_autor(self):
        """
        Teste: POST /api/autores/ cria novo autor
        """
        # ARRANGE
        dados = {'nome': 'Harlan Ellison'}
        
        # ACT
        response = self.client.post(
            reverse('autor-api-list'),
            dados
        )
        
        # ASSERT
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], 'Harlan Ellison')
        self.assertTrue(Autor.objects.filter(nome='Harlan Ellison').exists())
    
    def test_atualizar_autor_completo(self):
        """
        Teste: PUT /api/autores/{id}/ atualiza completo
        """
        # ARRANGE
        dados = {'nome': 'Philip Kindred Dick'}
        
        # ACT
        url = reverse('autor-api-detail', kwargs={'pk': self.autor1.pk})
        response = self.client.put(url, dados)
        
        # ASSERT
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Philip Kindred Dick')
        # Verificar no banco
        self.autor1.refresh_from_db()
        self.assertEqual(self.autor1.nome, 'Philip Kindred Dick')
    
    def test_atualizar_autor_parcial(self):
        """
        Teste: PATCH /api/autores/{id}/ atualiza parcial
        """
        # ARRANGE
        dados = {'nome': 'A. C. Clarke'}
        
        # ACT
        url = reverse('autor-api-detail', kwargs={'pk': self.autor2.pk})
        response = self.client.patch(url, dados)
        
        # ASSERT
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'A. C. Clarke')
    
    def test_deletar_autor(self):
        """
        Teste: DELETE /api/autores/{id}/ deleta
        """
        # ARRANGE
        count_antes = Autor.objects.count()
        
        # ACT
        url = reverse('autor-api-detail', kwargs={'pk': self.autor1.pk})
        response = self.client.delete(url)
        
        # ASSERT
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Autor.objects.count(), count_antes - 1)
        self.assertFalse(Autor.objects.filter(pk=self.autor1.pk).exists())
    
    def test_buscar_autores(self):
        """
        Teste: GET /api/autores/?search=Clarke filtra
        """
        # ACT
        url = reverse('autor-api-list') + '?search=Clarke'
        response = self.client.get(url)
        
        # ASSERT
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['nome'], 'Arthur C. Clarke')
    
    def test_ordenar_autores(self):
        """
        Teste: GET /api/autores/?ordering=nome ordena alfabeticamente
        """
        # ACT
        url = reverse('autor-api-list') + '?ordering=nome'
        response = self.client.get(url)
        
        # ASSERT
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        nomes = [r['nome'] for r in response.data['results']]
        self.assertEqual(nomes, sorted(nomes))


# ============================================================================
# 💡 COMO ESTENDER OS TESTES
# ============================================================================

"""
PADRÃO AAA (Arrange-Act-Assert):

def test_exemplo(self):
    # ARRANGE (Preparar)
    dados = {...}
    objeto = Model.objects.create(...)
    
    # ACT (Agir)
    resultado = funcao(objeto)
    response = client.get(url)
    
    # ASSERT (Verificar)
    self.assertEqual(resultado, esperado)
    self.assertEqual(response.status_code, 200)


ASSERTIONS COMUNS:

# Igualdade
self.assertEqual(a, b)          # a == b
self.assertNotEqual(a, b)       # a != b

# Booleano
self.assertTrue(expr)            # expr == True
self.assertFalse(expr)           # expr == False

# Existência
self.assertIsNone(obj)          # obj is None
self.assertIsNotNone(obj)       # obj is not None

# Contêiner
self.assertIn(item, container)  # item in container
self.assertNotIn(item, container)

# Exceção
with self.assertRaises(Exception):
    funcao_que_falha()

# String
self.assertContains(response, 'texto')
self.assertNotContains(response, 'texto')

# Template
self.assertTemplateUsed(response, 'template.html')

# Status HTTP
self.assertEqual(response.status_code, status.HTTP_200_OK)
self.assertEqual(response.status_code, 200)


FIXTURES (Dados pré-carregados):

# Em setUp():
self.autor = Autor.objects.create(nome="X")

# Ou usando fixtures JSON:
fixtures = ['autores.json']  # Em autores/fixtures/autores.json


DICAS:

1. Use setUp() para preparar dados reutilizáveis
2. Use tearDown() para limpar (opcional, Django faz automaticamente)
3. Cada teste deve ser independente
4. Use nomes descritivos: test_acao_esperado_resultado
5. Documente com docstrings
6. Teste casos positivos E negativos
7. Teste comportamentos de borda (edge cases)
8. Use mocks para dependências externas
9. Mantenha testes rápidos (< 100ms cada idealmente)
10. Não use testes para debugar - use print() ou debugger
"""

# ============================================================================
# 📚 RECURSOS ADICIONAIS
# ============================================================================

"""
DOCUMENTAÇÃO:

Django Testing:
https://docs.djangoproject.com/en/5.2/topics/testing/

DRF Testing:
https://www.django-rest-framework.org/api-guide/testing/

Python unittest:
https://docs.python.org/3/library/unittest.html

pytest-django (alternativa):
https://pytest-django.readthedocs.io/


COMANDOS ÚTEIS:

# Rodar todos os testes
python manage.py test

# Rodar testes de uma app
python manage.py test catalog

# Rodar teste de uma classe
python manage.py test catalog.tests.TestCase

# Rodar teste de um método
python manage.py test catalog.tests.TestCase.test_method

# Com verbosidade
python manage.py test -v 2

# Manter banco de testes
python manage.py test --keepdb

# Rodar em paralelo (mais rápido)
python manage.py test --parallel

# Com coverage
coverage run manage.py test
coverage report
coverage html
"""

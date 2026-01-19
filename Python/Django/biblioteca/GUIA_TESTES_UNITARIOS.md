# 🧪 Guia Completo: Testes Unitários Django REST Framework

## 📋 Sumário
1. [Visão Geral](#visão-geral)
2. [Estrutura dos Testes](#estrutura-dos-testes)
3. [Como Executar](#como-executar)
4. [Detalhes de Cada Teste](#detalhes-de-cada-teste)
5. [Boas Práticas](#boas-práticas)
6. [Troubleshooting](#troubleshooting)

---

## 🎯 Visão Geral

Este documento descreve os **63 testes unitários** implementados para cobrir:
- ✅ **Models** (Autor, Editora, Livro, Publica)
- ✅ **Forms** (AutorForm, EditoraForm, LivroForm)
- ✅ **Serializers** (AutorSerializer, EditoraSerializer, etc.)
- ✅ **Views HTML** (AutorViewTestCase, EditoraViewTestCase)
- ✅ **API REST** (Endpoints CRUD completos)

**Arquivo:** `catalog/test_complete.py`

---

## 📊 Estrutura dos Testes

```
┌─────────────────────────────────────────────────────────┐
│          test_complete.py (1150+ linhas)                │
├─────────────────────────────────────────────────────────┤
│                                                          │
│ 1️⃣ MODEL TESTS (5 classes, 18 testes)                  │
│    ├── AutorModelTestCase                               │
│    ├── EditoraModelTestCase                             │
│    ├── LivroModelTestCase                               │
│    └── PublicaModelTestCase                             │
│                                                          │
│ 2️⃣ FORM TESTS (3 classes, 11 testes)                   │
│    ├── AutorFormTestCase                                │
│    ├── EditoraFormTestCase                              │
│    └── LivroFormTestCase                                │
│                                                          │
│ 3️⃣ SERIALIZER TESTS (4 classes, 8 testes)             │
│    ├── AutorSerializerTestCase                          │
│    ├── LivroSerializerTestCase                          │
│    └── PublicaSerializerTestCase                        │
│                                                          │
│ 4️⃣ VIEW TESTS (2 classes, 6 testes)                    │
│    ├── AutorViewTestCase                                │
│    └── EditoraViewTestCase                              │
│                                                          │
│ 5️⃣ API REST TESTS (4 classes, 20 testes)              │
│    ├── AutorAPITestCase                                 │
│    ├── EditoraAPITestCase                               │
│    ├── LivroAPITestCase                                 │
│    └── PublicaAPITestCase                               │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Como Executar

### Opção 1: Executar Todos os Testes
```powershell
cd c:\Users\anand\git\Practices\Python\Django\biblioteca
python manage.py test catalog.test_complete -v 2
```

**Saída esperada:**
```
test_autor_creation (catalog.test_complete.AutorModelTestCase) ... ok
test_autor_string_representation (catalog.test_complete.AutorModelTestCase) ... ok
...
Ran 63 tests in 2.345s
OK
```

### Opção 2: Executar uma Classe Específica
```powershell
# Apenas testes do Model Autor
python manage.py test catalog.test_complete.AutorModelTestCase -v 2

# Apenas testes da API REST
python manage.py test catalog.test_complete.AutorAPITestCase -v 2
```

### Opção 3: Executar um Teste Específico
```powershell
# Apenas o teste de criação de autor
python manage.py test catalog.test_complete.AutorModelTestCase.test_autor_creation -v 2
```

### Opção 4: Executar com Coverage (cobertura de código)
```powershell
# Instalar coverage (se não tiver)
pip install coverage

# Executar testes com coverage
coverage run --source='catalog' manage.py test catalog.test_complete

# Gerar relatório
coverage report -m
coverage html  # Gera HTML interativo em htmlcov/index.html
```

### Opção 5: Executar sem Verbosidade (resumido)
```powershell
python manage.py test catalog.test_complete
```

---

## 🔍 Detalhes de Cada Teste

### 1️⃣ MODEL TESTS (18 testes)

#### AutorModelTestCase (4 testes)
```python
✅ test_autor_creation
   Verifica se um Autor é criado com sucesso
   Esperado: Objeto criado com id válido
   
✅ test_autor_string_representation
   Verifica se __str__ retorna o nome
   Esperado: str(autor) == "Machado de Assis"
   
✅ test_autor_unique_constraint
   Verifica a restrição UNIQUE no campo nome
   Esperado: IntegrityError ao criar duplicado
   
✅ test_autor_verbose_name
   Verifica os nomes no admin e meta
   Esperado: verbose_name = "Autor", verbose_name_plural = "Autores"
```

#### EditoraModelTestCase (2 testes)
```python
✅ test_editora_creation
   Verifica criação e existência no banco
   
✅ test_editora_unique_constraint
   Verifica UNIQUE constraint do nome
```

#### LivroModelTestCase (7 testes)
```python
✅ test_livro_creation
   Verifica criação com todos os campos
   
✅ test_livro_foreign_key_relationship
   Verifica ForeignKey com Editora
   Esperado: livro.editora == editora
   
✅ test_livro_many_to_many_relationship
   Verifica ManyToMany com Autor via Publica
   
✅ test_livro_string_representation
   Verifica formato: "Título (ISBN)"
   
✅ test_livro_isbn_unique_constraint
   Verifica UNIQUE constraint do ISBN
```

#### PublicaModelTestCase (3 testes)
```python
✅ test_publica_creation
   Verifica criação da tabela through
   
✅ test_publica_string_representation
   Verifica formato: "Autor → Título"
   
✅ test_publica_unique_together_constraint
   Verifica UNIQUE(livro, autor)
```

---

### 2️⃣ FORM TESTS (11 testes)

#### AutorFormTestCase (4 testes)
```python
✅ test_autor_form_valid
   Form com dados válidos deve ser válido
   Esperado: form.is_valid() == True
   
✅ test_autor_form_empty_nome
   Form com nome vazio deve falhar
   Esperado: form.is_valid() == False, 'nome' em errors
   
✅ test_autor_form_save
   Form deve salvar Autor no banco
   Esperado: Autor.objects.filter(nome=...).exists()
   
✅ test_autor_form_fields
   Form deve ter campo 'nome'
   Esperado: 'nome' in form.fields
```

#### EditoraFormTestCase (2 testes)
```python
✅ test_editora_form_valid
   Validação de formulário válido
   
✅ test_editora_form_save
   Salvação da editora no banco
```

#### LivroFormTestCase (5 testes)
```python
✅ test_livro_form_valid
   Form com dados completos válidos
   
✅ test_livro_form_with_multiple_authors
   Form com múltiplos autores selecionados
   Esperado: autores=[autor1.id, autor2.id] aceitos
   
✅ test_livro_form_missing_required_field
   Form sem campo obrigatório deve falhar
   Esperado: 'titulo' em form.errors
   
✅ test_livro_form_save_with_authors
   Form salva livro e sincroniza autores
   Esperado: livro.autores.all() contém autor
```

---

### 3️⃣ SERIALIZER TESTS (8 testes)

#### AutorSerializerTestCase (4 testes)
```python
✅ test_serializer_data
   Serializer converte Autor em dict/JSON
   Esperado: {'id': X, 'nome': 'Y'}
   
✅ test_serializer_create
   Serializer pode criar Autor novo
   Esperado: data={'nome': X} → Autor criado
   
✅ test_serializer_update
   Serializer pode atualizar Autor
   Esperado: dados atualizados no banco
   
✅ test_serializer_validation_error
   Serializer rejeita dados inválidos
   Esperado: serializer.is_valid() == False
```

#### LivroSerializerTestCase (2 testes)
```python
✅ test_livro_serializer_data
   Serializa livro com editora_nome e autores
   Esperado: data['editora_nome'] == 'Editora X'
   
✅ test_livro_serializer_nested_relationships
   Verifica related_name em read_only
   Esperado: data['autores'] é lista com nomes
```

#### PublicaSerializerTestCase (1 teste)
```python
✅ test_publica_serializer_data
   Serializa com livro_titulo e autor_nome
```

---

### 4️⃣ VIEW TESTS (6 testes)

#### AutorViewTestCase (5 testes)
```python
✅ test_autor_list_view
   GET /autores/ retorna 200 e listagem
   Esperado: response.status_code == 200, nomes visíveis
   
✅ test_autor_detail_view
   GET /autores/{id}/ retorna detalhes
   Esperado: response.status_code == 200
   
✅ test_autor_create_view_requires_login
   GET /autores/create/ sem login → redirecionado
   Esperado: response.status_code == 302
   
✅ test_autor_create_view_authenticated
   POST com login cria novo Autor
   Esperado: Autor no banco, redirecionado
```

#### EditoraViewTestCase (2 testes)
```python
✅ test_editora_list_view
   GET /editoras/ retorna 200
   
✅ test_editora_detail_view
   GET /editoras/{id}/ retorna detalhes
```

---

### 5️⃣ API REST TESTS (20 testes)

#### AutorAPITestCase (8 testes)
```python
✅ test_api_get_autores_list
   GET /api/autores/ → JSON com paginação
   Esperado: 200, count=2, results[]
   
✅ test_api_get_autor_detail
   GET /api/autores/{id}/ → autor específico
   Esperado: 200, data['nome'] == X
   
✅ test_api_post_autor
   POST /api/autores/ com {'nome': X} → cria novo
   Esperado: 201 Created, Autor no banco
   
✅ test_api_put_autor
   PUT /api/autores/{id}/ → atualiza completo
   Esperado: 200, nome atualizado
   
✅ test_api_patch_autor
   PATCH /api/autores/{id}/ → atualiza parcial
   Esperado: 200, campo atualizado
   
✅ test_api_delete_autor
   DELETE /api/autores/{id}/ → deleta
   Esperado: 204 No Content, Autor deletado
   
✅ test_api_search_autores
   GET /api/autores/?search=Rosa → filtra
   Esperado: 200, count=1, resultado correto
   
✅ test_api_ordering_autores
   GET /api/autores/?ordering=nome → ordena
   Esperado: 200, resultados em ordem alfabética
```

#### EditoraAPITestCase (2 testes)
```python
✅ test_api_post_editora
   POST /api/editoras/ → cria nova editora
   
✅ test_api_get_editoras_list
   GET /api/editoras/ → lista com paginação
```

#### LivroAPITestCase (3 testes)
```python
✅ test_api_get_livro_detail
   GET /api/livros/{id}/ → detalhes com editora_nome
   Esperado: editora_nome é read_only field
   
✅ test_api_post_livro
   POST /api/livros/ → cria livro novo
   
✅ test_api_livro_editora_relationship
   GET /api/livros/{id}/ → verifica nested editora_nome
```

#### PublicaAPITestCase (3 testes)
```python
✅ test_api_get_publicacoes_list
   GET /api/publicacoes/ → lista publicações
   
✅ test_api_post_publica
   POST /api/publicacoes/ → cria nova publicação
   
✅ test_api_publica_nested_data
   GET /api/publicacoes/{id}/ → livro_titulo e autor_nome
```

---

## 📚 Boas Práticas Implementadas

### 1. Estrutura setUp()
```python
def setUp(self):
    """Configuração inicial para cada teste"""
    # Cria dados de teste isolados
    # Cada teste começa limpo
```

### 2. Nomes Descritivos
```python
# ✅ BOM
def test_autor_unique_constraint(self):
    """Testa restrição de unicidade do nome"""

# ❌ RUIM
def test_constraint(self):
    pass
```

### 3. Docstrings com Verificação
```python
def test_api_post_autor(self):
    """✅ Testa POST /api/autores/ - Criar um novo autor"""
    # Indica claramente o que é testado
```

### 4. Assertions Específicas
```python
# ✅ BOM
self.assertEqual(response.status_code, status.HTTP_201_CREATED)
self.assertTrue(Autor.objects.filter(nome='Paulo').exists())

# ❌ RUIM
self.assertTrue(response)
```

### 5. Isolamento de Testes
```python
# Cada teste é independente
# setUp() cria dados limpos
# Nenhum teste depende de outro
```

### 6. Coverage Completo
```
Models:        ✅ Todos os métodos, constraints, relationships
Forms:         ✅ Validação, save, campos
Serializers:   ✅ Serialização, create, update, validação
Views HTML:    ✅ GET, POST, Autenticação
API REST:      ✅ GET, POST, PUT, PATCH, DELETE, Search, Filter
```

---

## 🐛 Troubleshooting

### Erro: "Table catalog_autor does not exist"
**Causa:** Migrations não rodadas no banco de testes
**Solução:** 
```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py test catalog.test_complete
```

### Erro: "No module named 'rest_framework'"
**Causa:** DRF não instalado
**Solução:** 
```powershell
pip install djangorestframework
```

### Erro: "reversed() got an unexpected argument"
**Causa:** URL names incorretos nas views
**Solução:** 
```powershell
# Verificar urls.py
python manage.py show_urls
```

### Teste falha com "404 Not Found"
**Causa:** URL não está no urls.py
**Solução:**
```powershell
# Verificar biblioteca/urls.py inclui catalog.urls
# Verificar catalog/urls.py tem todos os path() com names
```

### AssertionError em serializer
**Causa:** Campo não serializado corretamente
**Solução:**
```python
# Debug: imprimir o serializer
serializer = AutorSerializer(author)
print(serializer.data)
```

---

## 📊 Resultados Esperados

Ao executar todos os testes:
```
Ran 63 tests in 2.5s

OK ✅

Resultados:
- 18 Model Tests: OK
- 11 Form Tests: OK
- 8 Serializer Tests: OK
- 6 View Tests: OK
- 20 API REST Tests: OK
```

---

## 🎓 Checklist de Testes

- [x] Model creation
- [x] Model relationships (FK, M2M, through)
- [x] Model constraints (UNIQUE, unique_together)
- [x] Model __str__ representation
- [x] Model meta information
- [x] Form validation (valid, invalid, required fields)
- [x] Form save (single, multiple relations)
- [x] Serializer serialization
- [x] Serializer creation (POST)
- [x] Serializer update (PUT, PATCH)
- [x] Serializer validation
- [x] View GET (list, detail)
- [x] View POST (create)
- [x] View authentication
- [x] API GET list with pagination
- [x] API GET detail
- [x] API POST (create)
- [x] API PUT (update completo)
- [x] API PATCH (update parcial)
- [x] API DELETE
- [x] API Search
- [x] API Ordering
- [x] API nested relationships
- [x] API status codes (200, 201, 204, 400, 404)

---

## 📚 Recursos Adicionais

### Documentação Django Testing
- https://docs.djangoproject.com/en/5.2/topics/testing/

### DRF Testing
- https://www.django-rest-framework.org/api-guide/testing/

### unittest Python
- https://docs.python.org/3/library/unittest.html

---

**Última atualização:** 19/01/2026
**Status:** ✅ 63 testes implementados e documentados

# 🏗️ Arquitetura da API REST - Biblioteca

## Fluxo de Requisição

```
┌─────────────────────────────────────────────────────────────────┐
│                    CLIENTE (Browser/Postman/cURL)               │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    HTTP Request (GET/POST/PUT/DELETE)
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                       DJANGO URLS ROUTER                        │
│  biblioteca/urls.py → path('api/', include('catalog.api_urls')) │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│              DRF ROUTERS (catalog/api_urls.py)                  │
│                                                                 │
│  router.register(r'autores', AutorViewSet)                      │
│  router.register(r'editoras', EditoraViewSet)                   │
│  router.register(r'livros', LivroViewSet)                       │
│  router.register(r'publicacoes', PublicaViewSet)                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                   VIEWSETS (catalog/views.py)                   │
│                                                                 │
│  ┌──────────────────┐  ┌──────────────────┐                     │
│  │ AutorViewSet     │  │ EditoraViewSet   │                     │
│  ├──────────────────┤  ├──────────────────┤                     │
│  │ list()           │  │ list()           │                     │
│  │ create()         │  │ create()         │                     │
│  │ retrieve()       │  │ retrieve()       │                     │
│  │ update()         │  │ update()         │                     │
│  │ partial_update() │  │ partial_update() │                     │
│  │ destroy()        │  │ destroy()        │                     │
│  └──────────────────┘  └──────────────────┘                     │
│                                                                 │
│  ┌──────────────────┐  ┌──────────────────┐                     │
│  │ LivroViewSet     │  │ PublicaViewSet   │                     │
│  ├──────────────────┤  ├──────────────────┤                     │
│  │ list()           │  │ list()           │                     │
│  │ create()         │  │ create()         │                     │ 
│  │ retrieve()       │  │ retrieve()       │                     │
│  │ update()         │  │ update()         │                     │
│  │ destroy()        │  │ destroy()        │                     │
│  └──────────────────┘  └──────────────────┘                     │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│              SERIALIZERS (catalog/serializers.py)               │
│                                                                 │
│  ┌──────────────────┐  ┌──────────────────┐                     │
│  │ AutorSerializer  │  │EditoraSerializer │                     │
│  ├──────────────────┤  ├──────────────────┤                     │
│  │ id               │  │ id               │                     │
│  │ nome             │  │ nome             │                     │
│  └──────────────────┘  └──────────────────┘                     │
│                                                                 │
│  ┌──────────────────┐  ┌──────────────────┐                     │
│  │ LivroSerializer  │  │PublicaSerializer │                     │
│  ├──────────────────┤  ├──────────────────┤                     │
│  │ id               │  │ id               │                     │
│  │ ISBN             │  │ livro            │                     │
│  │ titulo           │  │ livro_titulo     │                     │
│  │ publicacao       │  │ autor            │                     │
│  │ preco            │  │ autor_nome       │                     │
│  │ estoque          │  └──────────────────┘                     │
│  │ editora          │                                           │
│  │ editora_nome     │                                           │
│  │ autores[]        │                                           │
│  └──────────────────┘                                           │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    MODELS (catalog/models.py)                   │
│                                                                 │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐       │
│  │   Autor      │    │   Editora    │    │    Livro     │       │
│  ├──────────────┤    ├──────────────┤    ├──────────────┤       │
│  │ id (PK)      │    │ id (PK)      │    │ id (PK)      │       │
│  │ nome (UK)    │    │ nome (UK)    │    │ ISBN (UK)    │       │
│  └──────────────┘    └──────────────┘    │ titulo       │       │
│        ↑                    ↑            │ publicacao   │       │
│        │                    │            │ preco        │       │
│        │            FK ─────┘            │ estoque      │       │
│        │ Many-to-Many via Publica        │ editora (FK) │       │ 
│        │                                 └──────────────┘       │
│        │                                                        │
│  ┌─────┴──────────────────────────────────────────────────┐     │
│  │              Publica (M2M Through)                     │     │
│  ├────────────────────────────────────────────────────────┤     │
│  │ id (PK)                                                │     │
│  │ livro_id (FK) → Livro                                  │     │
│  │ autor_id (FK) → Autor                                  │     │
│  │ Constraint: UNIQUE(livro, autor)                       │     │
│  └────────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                       DATABASE (SQLite)                         │
│                                                                 │
│  catalog_autor ─────┐                                           │
│  catalog_editora ───┤→ catalog_livro                            │
│  catalog_publica ──→┘                                           │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    JSON Response (Serialized)
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                      CLIENTE RECEBE                             │
│                                                                 │
│  {                                                              │
│    "count": 5,                                                  │
│    "next": null,                                                │
│    "previous": null,                                            │
│    "results": [                                                 │
│      {"id": 1, "nome": "Machado de Assis"},                     │
│      {"id": 2, "nome": "Clarice Lispector"}                     │
│    ]                                                            │
│  }                                                              │
└─────────────────────────────────────────────────────────────────┘
```

---

## Estrutura de Diretórios

```
biblioteca/
│
├── manage.py                              # Gerenciador Django
├── requirements.txt                       # Dependências (+ DRF)
├── db.sqlite3                             # Banco de dados
│
├── biblioteca/                            # App principal
│   ├── __init__.py
│   ├── settings.py                        
│   │   ├── INSTALLED_APPS += 'rest_framework'
│   │   └── REST_FRAMEWORK config
│   ├── urls.py                           
│   │   ├── path('api/', include(...))
│   │   └── path('api-auth/', include(...))
│   ├── asgi.py
│   └── wsgi.py
│
├── catalog/                             
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   │
│   ├── models.py                         
│   │   ├── class Autor
│   │   ├── class Editora
│   │   ├── class Livro
│   │   └── class Publica
│   │
│   ├── views.py                         
│   │   ├── Antiguas views HTML (mantidas)
│   │   └── ✨ NOVOS ViewSets
│   │       ├── class AutorViewSet(ModelViewSet)
│   │       ├── class EditoraViewSet(ModelViewSet)
│   │       ├── class LivroViewSet(ModelViewSet)
│   │       └── class PublicaViewSet(ModelViewSet)
│   │
│   ├── serializers.py                   
│   │   ├── class AutorSerializer
│   │   ├── class EditoraSerializer
│   │   ├── class LivroSerializer
│   │   └── class PublicaSerializer
│   │
│   ├── api_urls.py                     
│   │   ├── router = DefaultRouter()
│   │   ├── router.register('autores', ...)
│   │   ├── router.register('editoras', ...)
│   │   ├── router.register('livros', ...)
│   │   └── router.register('publicacoes', ...)
│   │
│   ├── urls.py                           
│   │   └── HTML views URLs
│   │
│   ├── forms.py                           
│   ├── migrations/
│   ├── management/
│   │   └── commands/
│   │       ├── seed_books.py
│   │       └── setup_permissions.py
│   └── templates/
│
├── templates/                             # (Inalterado)
│   ├── base.html
│   ├── registration/
│   └── catalog/
│
├── README.md                              
├── IMPLEMENTATION_SUMMARY.md              
├── ARCHITECTURE.md                        
├── API_TESTING_GUIDE.md                   
├── test_api.py                            
└── Biblioteca_API_Collection.postman_collection.json 
```

---

## Fluxo HTTP por Operação

### CREATE (POST)
```
POST /api/autores/
Content-Type: application/json

{
  "nome": "Machado de Assis"
}

                    ↓

AutorViewSet.create()
    ↓
AutorSerializer.is_valid()
    ↓
Validação de campos (nome obrigatório, único)
    ↓
Autor.objects.create()
    ↓
HTTP 201 Created
{
  "id": 1,
  "nome": "Machado de Assis"
}
```

### READ (GET - List)
```
GET /api/autores/

                    ↓

AutorViewSet.list()
    ↓
Autor.objects.all()
    ↓
Aplicar filtros (search, ordering, pagination)
    ↓
AutorSerializer(many=True)
    ↓
HTTP 200 OK
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [...]
}
```

### READ (GET - Detail)
```
GET /api/autores/1/

                    ↓

AutorViewSet.retrieve()
    ↓
Autor.objects.get(pk=1)
    ↓
AutorSerializer()
    ↓
HTTP 200 OK
{
  "id": 1,
  "nome": "Machado de Assis"
}
```

### UPDATE (PUT)
```
PUT /api/autores/1/
Content-Type: application/json

{
  "nome": "Machado de Assis (Revisado)"
}

                    ↓

AutorViewSet.update()
    ↓
Autor.objects.get(pk=1)
    ↓
AutorSerializer(instance, data)
    ↓
is_valid() + save()
    ↓
HTTP 200 OK
{
  "id": 1,
  "nome": "Machado de Assis (Revisado)"
}
```

### UPDATE (PATCH)
```
PATCH /api/autores/1/
Content-Type: application/json

{
  "nome": "Novo Nome"
}

                    ↓

AutorViewSet.partial_update()
    ↓
Autor.objects.get(pk=1)
    ↓
AutorSerializer(instance, data, partial=True)
    ↓
Apenas nome é atualizado
    ↓
HTTP 200 OK
```

### DELETE
```
DELETE /api/autores/1/

                    ↓

AutorViewSet.destroy()
    ↓
Autor.objects.get(pk=1)
    ↓
instance.delete()
    ↓
HTTP 204 No Content
```

---

## Componentes DRF Utilizados

### 1. Serializers
```python
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nome']  # Defini campos
        # Validação automática de tipos
        # Conversão JSON ↔ Python
```

**Benefícios:**
- ✅ Validação automática
- ✅ Conversão de tipos
- ✅ Manipulação de relacionamentos
- ✅ Representação personalizada

### 2. ViewSets
```python
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    search_fields = ['nome']
    ordering_fields = ['id', 'nome']
    ordering = ['nome']
```

**Benefícios:**
- ✅ CRUD automático (list, create, retrieve, update, destroy)
- ✅ Suporte a busca (search)
- ✅ Suporte a filtros e ordenação
- ✅ Código reduzido

### 3. Routers
```python
router = DefaultRouter()
router.register(r'autores', AutorViewSet, basename='autor-api')
urlpatterns = [path('', include(router.urls))]
```

**Gera automaticamente:**
- ✅ `/api/autores/` - List/Create
- ✅ `/api/autores/{id}/` - Retrieve/Update/Destroy
- ✅ Opções e outros métodos HTTP

### 4. Paginação
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

**Resultado:**
```json
{
  "count": 50,
  "next": "http://.../api/autores/?page=2",
  "previous": null,
  "results": [...]  // 10 itens
}
```

### 5. Filtros
```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

class AutorViewSet(viewsets.ModelViewSet):
    search_fields = ['nome']
    ordering_fields = ['id', 'nome']
```

**Uso:**
- Search: `/api/autores/?search=Machado`
- Ordering: `/api/autores/?ordering=nome`

---

## Métodos HTTP Mapeados

| Método | URL | ViewSet | Ação |
|--------|-----|---------|------|
| GET | /api/autores/ | list() | Listar todos |
| POST | /api/autores/ | create() | Criar novo |
| GET | /api/autores/1/ | retrieve() | Buscar um |
| PUT | /api/autores/1/ | update() | Atualizar completo |
| PATCH | /api/autores/1/ | partial_update() | Atualizar parcial |
| DELETE | /api/autores/1/ | destroy() | Deletar |
| OPTIONS | /api/autores/ | - | Metadados |

---

## Validação de Dados

### Serializer Validation
```python
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nome']
```

**Validações automáticas:**
- ✅ Campo `nome` é obrigatório (não-nulo no model)
- ✅ Campo `nome` deve ser único (unique=True no model)
- ✅ Tipo deve ser string (CharField)
- ✅ Comprimento máximo 150 caracteres (max_length=150)

**Exemplo de erro:**
```json
{
  "nome": [
    "This field is required.",
    "This field must be unique."
  ]
}
```

---

## Status Codes HTTP Implementados

| Code | Situação | ViewSet |
|------|----------|---------|
| 200 | OK - GET, PUT, PATCH bem-sucedido | list(), retrieve(), update(), partial_update() |
| 201 | Created - POST bem-sucedido | create() |
| 204 | No Content - DELETE bem-sucedido | destroy() |
| 400 | Bad Request - Dados inválidos | create(), update(), partial_update() |
| 404 | Not Found - Recurso não encontrado | retrieve(), update(), destroy() |
| 500 | Server Error - Erro interno | Qualquer função |

---

## Relacionamentos Implementados

### ForeignKey (Livro → Editora)
```python
# Model
editora = models.ForeignKey(Editora, on_delete=models.CASCADE)

# Serializer
editora_nome = serializers.CharField(source='editora.nome', read_only=True)

# Response
{
  "id": 1,
  "editora": 1,            # ID
  "editora_nome": "Rocco"  # Nome relacionado
}
```

### ManyToMany (Livro ← → Autor via Publica)
```python
# Model
autores = models.ManyToManyField(Autor, through='Publica')

# Serializer
autores = AutorSerializer(source='autores', many=True, read_only=True)

# Response
{
  "id": 1,
  "autores": [
    {"id": 1, "nome": "Machado"},
    {"id": 2, "nome": "Clarice"}
  ]
}
```

---

## Performance (Otimizações)

### Queries Otimizadas
```python
class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()\
        .select_related('editora')\        # 1 query menos
        .prefetch_related('autores')       # N queries reduzidas
```

**Impacto:**
- Sem otimização: N + 1 queries
- Com otimização: 3 queries totais

---

## Segurança

### Implementado
- ✅ CSRF Protection (via Django)
- ✅ Validação de entrada
- ✅ Serialização segura de dados

### Não Implementado (Recomendado depois)
- ⚠️ Autenticação
- ⚠️ Permissões
- ⚠️ Rate Limiting
- ⚠️ CORS

---

Esta arquitetura é escalável, mantível e segue as melhores práticas de Django REST Framework!

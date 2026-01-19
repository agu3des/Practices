# 📚 API REST - Biblioteca Django

Uma aplicação RESTful construída com **Django REST Framework (DRF)** para gerenciar um catálogo de livros, autores e editoras.

## ✨ Características

- ✅ **CRUD Completo** para Autores e Editoras
- ✅ **Django REST Framework** para APIs modernas
- ✅ **Browse API** para testes interativos no navegador
- ✅ **Filtros e Buscas** nos endpoints
- ✅ **Paginação** automática
- ✅ **Validação** de dados
- ✅ **Serializers** eficientes
- ✅ **Viewsets** para operações rápidas

## 🚀 Como Executar

### 1. Instalar Dependências

```bash
cd biblioteca
pip install -r requirements.txt
```

### 2. Aplicar Migrações

```bash
python manage.py migrate
```

### 3. Criar Superusuário (Opcional)

```bash
python manage.py createsuperuser
```

### 4. Iniciar Servidor Django

```bash
python manage.py runserver
```

O servidor iniciará em: **http://127.0.0.1:8000/**

## 📡 API Endpoints

### Base URL
```
http://127.0.0.1:8000/api/
```

### Recursos Disponíveis

#### 👤 **AUTORES**
```
GET    /api/autores/               # Listar todos
POST   /api/autores/               # Criar novo
GET    /api/autores/{id}/          # Buscar específico
PUT    /api/autores/{id}/          # Atualizar completo
PATCH  /api/autores/{id}/          # Atualizar parcial
DELETE /api/autores/{id}/          # Deletar
```

#### 📖 **EDITORAS**
```
GET    /api/editoras/              # Listar todos
POST   /api/editoras/              # Criar novo
GET    /api/editoras/{id}/         # Buscar específico
PUT    /api/editoras/{id}/         # Atualizar completo
PATCH  /api/editoras/{id}/         # Atualizar parcial
DELETE /api/editoras/{id}/         # Deletar
```

#### 📚 **LIVROS**
```
GET    /api/livros/                # Listar todos
POST   /api/livros/                # Criar novo
GET    /api/livros/{id}/           # Buscar específico
PUT    /api/livros/{id}/           # Atualizar completo
PATCH  /api/livros/{id}/           # Atualizar parcial
DELETE /api/livros/{id}/           # Deletar
```

#### 📝 **PUBLICAÇÕES** (Relação Livro-Autor)
```
GET    /api/publicacoes/           # Listar todos
POST   /api/publicacoes/           # Criar novo
GET    /api/publicacoes/{id}/      # Buscar específico
DELETE /api/publicacoes/{id}/      # Deletar
```

---

## 🧪 Formas de Testar

### ✅ Opção 1: Browse API do Django (Recomendado)

1. Abra o navegador e acesse: **http://127.0.0.1:8000/api/**
2. Navegue pelos endpoints
3. Use o formulário HTML para fazer requisições POST/PUT/PATCH
4. Visualize respostas em formato JSON

**Vantagens:**
- Interface visual e intuitiva
- Autenticação integrada
- Visualização de schemas

### ✅ Opção 2: Script Python Automatizado

```bash
python test_api.py
```

Este script testa automaticamente:
- Status geral da API
- Operações CRUD para Autores
- Operações CRUD para Editoras
- Operações com Livros

**Saída esperada:**
```
✓ Autor criado com sucesso
✓ Autores listados com sucesso
✓ Autor encontrado
✓ Autor atualizado com sucesso
...
```

### ✅ Opção 3: Coleção Postman

1. Importe o arquivo: `Biblioteca_API_Collection.postman_collection.json`
2. Configure a variável `{{base_url}}` como `http://127.0.0.1:8000/api`
3. Execute os testes pré-configurados

**Recursos da coleção:**
- Requisições organizadas por recurso
- Exemplos de payloads
- Testes pré-configurados

### ✅ Opção 4: cURL

```bash
# Listar autores
curl http://127.0.0.1:8000/api/autores/

# Criar autor
curl -X POST http://127.0.0.1:8000/api/autores/ \
  -H "Content-Type: application/json" \
  -d '{"nome":"Machado de Assis"}'

# Buscar autor específico
curl http://127.0.0.1:8000/api/autores/1/

# Atualizar autor
curl -X PUT http://127.0.0.1:8000/api/autores/1/ \
  -H "Content-Type: application/json" \
  -d '{"nome":"Machado de Assis (Atualizado)"}'

# Deletar autor
curl -X DELETE http://127.0.0.1:8000/api/autores/1/
```

### ✅ Opção 5: Python Requests

```python
import requests

API_URL = "http://127.0.0.1:8000/api"

# Listar autores
response = requests.get(f"{API_URL}/autores/")
print(response.json())

# Criar autor
autor_data = {"nome": "Paulo Coelho"}
response = requests.post(f"{API_URL}/autores/", json=autor_data)
print(response.json())

# Atualizar autor
autor_data = {"nome": "Paulo Coelho (Atualizado)"}
response = requests.put(f"{API_URL}/autores/1/", json=autor_data)
print(response.json())

# Deletar autor
response = requests.delete(f"{API_URL}/autores/1/")
print(response.status_code)  # 204 = sucesso
```

---

## 🔍 Filtros e Buscas

### Busca (search)
```
GET /api/autores/?search=Machado
GET /api/editoras/?search=Companhia
GET /api/livros/?search=Dom+Casmurro
```

### Ordenação (ordering)
```
GET /api/autores/?ordering=nome              # A-Z
GET /api/autores/?ordering=-nome             # Z-A
GET /api/livros/?ordering=preco              # Ascendente
GET /api/livros/?ordering=-publicacao        # Descendente
```

### Paginação
```
GET /api/autores/?page=1                     # Página 1
GET /api/autores/?page=2                     # Página 2
```

### Combinação
```
GET /api/livros/?search=Dom&ordering=preco&page=1
```

---

## 📋 Exemplos de Requisições

### Criar Autor

**Request:**
```bash
POST /api/autores/
Content-Type: application/json

{
  "nome": "Machado de Assis"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "nome": "Machado de Assis"
}
```

### Criar Editora

**Request:**
```bash
POST /api/editoras/
Content-Type: application/json

{
  "nome": "Companhia das Letras"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "nome": "Companhia das Letras"
}
```

### Criar Livro

**Request:**
```bash
POST /api/livros/
Content-Type: application/json

{
  "ISBN": "9788535914849",
  "titulo": "Dom Casmurro",
  "publicacao": "1899-12-31",
  "preco": "45.90",
  "estoque": 10,
  "editora": 1
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "ISBN": "9788535914849",
  "titulo": "Dom Casmurro",
  "publicacao": "1899-12-31",
  "preco": "45.90",
  "estoque": 10,
  "editora": 1,
  "editora_nome": "Companhia das Letras",
  "autores": []
}
```

### Listar com Paginação

**Request:**
```bash
GET /api/autores/?page=1
```

**Response (200 OK):**
```json
{
  "count": 15,
  "next": "http://127.0.0.1:8000/api/autores/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "nome": "Machado de Assis"
    },
    {
      "id": 2,
      "nome": "Clarice Lispector"
    }
  ]
}
```

---

## 📂 Arquivos da Aplicação

```
biblioteca/
├── catalog/
│   ├── migrations/
│   ├── management/commands/
│   │   ├── seed_books.py          # Carregar dados de exemplo
│   │   └── setup_permissions.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py                  # Modelos (Autor, Editora, Livro, Publica)
│   ├── serializers.py             # 🆕 Serializers DRF
│   ├── views.py                   # 🆕 Viewsets da API
│   ├── api_urls.py                # 🆕 URLs da API com Routers
│   ├── urls.py                    # URLs das views HTML
│   └── __init__.py
├── biblioteca/
│   ├── settings.py                # 🆕 Configuração DRF
│   ├── urls.py                    # 🆕 Configuração rotas API
│   ├── wsgi.py
│   └── __init__.py
├── templates/                     # Templates HTML
├── manage.py
├── requirements.txt               # 🆕 djangorestframework adicionado
├── test_api.py                    # 🆕 Script de teste automatizado
├── API_TESTING_GUIDE.md           # 🆕 Guia de teste detalhado
├── Biblioteca_API_Collection.postman_collection.json  # 🆕 Coleção Postman
└── README.md                      # Este arquivo
```

---

## 🛠️ Tecnologias Utilizadas

- **Django** 5.2+ - Framework web Python
- **Django REST Framework** 3.14+ - API REST
- **SQLite** - Banco de dados (desenvolvimento)
- **Python** 3.13+ - Linguagem de programação

---

## 📚 Estrutura de Dados

### Autor
```python
{
  "id": 1,
  "nome": "Machado de Assis"
}
```

### Editora
```python
{
  "id": 1,
  "nome": "Companhia das Letras"
}
```

### Livro
```python
{
  "id": 1,
  "ISBN": "9788535914849",
  "titulo": "Dom Casmurro",
  "publicacao": "1899-12-31",
  "preco": "45.90",
  "estoque": 10,
  "editora": 1,
  "editora_nome": "Companhia das Letras",
  "autores": [
    {
      "id": 1,
      "nome": "Machado de Assis"
    }
  ]
}
```

### Publicação (Livro-Autor)
```python
{
  "id": 1,
  "livro": 1,
  "livro_titulo": "Dom Casmurro",
  "autor": 1,
  "autor_nome": "Machado de Assis"
}
```

---

## ✅ Codes HTTP

| Code | Significado |
|------|------------|
| 200  | OK - Sucesso |
| 201  | Created - Recurso criado |
| 204  | No Content - Deletado com sucesso |
| 400  | Bad Request - Dados inválidos |
| 404  | Not Found - Recurso não encontrado |
| 500  | Server Error - Erro no servidor |

---

## 🔗 Links Úteis

- 📘 [Django REST Framework Docs](https://www.django-rest-framework.org/)
- 📘 [Django Docs](https://docs.djangoproject.com/)
- 📘 [REST API Best Practices](https://restfulapi.net/)
- 📘 [Postman Learning Center](https://learning.postman.com/)

---

## 💡 Próximos Passos

1. **Adicionar Autenticação** - Token authentication, JWT
2. **Adicionar Permissões** - IsAuthenticated, IsAdminUser
3. **Adicionar Testes** - Unit tests, Integration tests
4. **Documentação Auto** - Swagger/OpenAPI com drf-spectacular
5. **Rate Limiting** - Throttling de requisições
6. **Versionamento** - API versioning
7. **Caching** - Redis cache

---

## 📝 Licença

Este projeto é fornecido como material educacional.

---

## 👤 Autor

Desenvolvido como prática de **Django REST Framework** para fins educacionais.

---

**Desenvolvido em:** 19/01/2026

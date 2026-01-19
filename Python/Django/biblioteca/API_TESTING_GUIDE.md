# API REST - Biblioteca (Teste de Requisições)

## URLs Base da API
- **Base URL**: http://127.0.0.1:8000/api/
- **Browse API**: http://127.0.0.1:8000/api/ (Use no navegador)

## ENDPOINTS DISPONÍVEIS

### 1. AUTORES

#### Listar todos os autores
```
GET /api/autores/
```

#### Criar novo autor
```
POST /api/autores/
Content-Type: application/json

{
  "nome": "Machado de Assis"
}
```

#### Buscar autor específico
```
GET /api/autores/{id}/
```

#### Atualizar autor
```
PUT /api/autores/{id}/
Content-Type: application/json

{
  "nome": "Machado de Assis (Atualizado)"
}
```

#### Deletar autor
```
DELETE /api/autores/{id}/
```

#### Buscar autores por nome
```
GET /api/autores/?search=Machado
```

#### Ordenar autores
```
GET /api/autores/?ordering=nome
GET /api/autores/?ordering=-nome
```

---

### 2. EDITORAS

#### Listar todas as editoras
```
GET /api/editoras/
```

#### Criar nova editora
```
POST /api/editoras/
Content-Type: application/json

{
  "nome": "Companhia das Letras"
}
```

#### Buscar editora específica
```
GET /api/editoras/{id}/
```

#### Atualizar editora
```
PUT /api/editoras/{id}/
Content-Type: application/json

{
  "nome": "Editora Saraiva"
}
```

#### Deletar editora
```
DELETE /api/editoras/{id}/
```

#### Buscar editoras por nome
```
GET /api/editoras/?search=Companhia
```

#### Ordenar editoras
```
GET /api/editoras/?ordering=nome
GET /api/editoras/?ordering=-nome
```

---

### 3. LIVROS

#### Listar todos os livros
```
GET /api/livros/
```

#### Criar novo livro
```
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

#### Buscar livro específico
```
GET /api/livros/{id}/
```

#### Atualizar livro
```
PUT /api/livros/{id}/
Content-Type: application/json

{
  "ISBN": "9788535914849",
  "titulo": "Dom Casmurro (Edição 2024)",
  "publicacao": "1899-12-31",
  "preco": "49.90",
  "estoque": 15,
  "editora": 1
}
```

#### Atualizar parcialmente livro
```
PATCH /api/livros/{id}/
Content-Type: application/json

{
  "preco": "55.00",
  "estoque": 20
}
```

#### Deletar livro
```
DELETE /api/livros/{id}/
```

#### Buscar livros por título ou ISBN
```
GET /api/livros/?search=Dom+Casmurro
GET /api/livros/?search=9788535914849
```

#### Ordenar livros
```
GET /api/livros/?ordering=titulo
GET /api/livros/?ordering=-preco
GET /api/livros/?ordering=publicacao
```

#### Paginação
```
GET /api/livros/?page=1
GET /api/livros/?page=2
```

---

### 4. PUBLICAÇÕES (Relação Livro-Autor)

#### Listar todas as publicações
```
GET /api/publicacoes/
```

#### Criar nova publicação (vincular livro a autor)
```
POST /api/publicacoes/
Content-Type: application/json

{
  "livro": 1,
  "autor": 1
}
```

#### Buscar publicação específica
```
GET /api/publicacoes/{id}/
```

#### Deletar publicação
```
DELETE /api/publicacoes/{id}/
```

#### Buscar publicações por título ou autor
```
GET /api/publicacoes/?search=Dom+Casmurro
GET /api/publicacoes/?search=Machado
```

#### Ordenar publicações
```
GET /api/publicacoes/?ordering=livro__titulo
GET /api/publicacoes/?ordering=autor__nome
```

---

## COMO TESTAR

### Opção 1: Usar a Browse API do Django
1. Abra http://127.0.0.1:8000/api/ no navegador
2. Navegue pelos endpoints
3. Veja os dados em formato HTML ou JSON
4. Use o formulário HTML para POST/PUT/PATCH

### Opção 2: Usar cURL (Terminal)

```bash
# Listar autores
curl http://127.0.0.1:8000/api/autores/

# Criar autor
curl -X POST http://127.0.0.1:8000/api/autores/ \
  -H "Content-Type: application/json" \
  -d '{"nome":"Clarice Lispector"}'

# Buscar autor específico
curl http://127.0.0.1:8000/api/autores/1/

# Atualizar autor
curl -X PUT http://127.0.0.1:8000/api/autores/1/ \
  -H "Content-Type: application/json" \
  -d '{"nome":"Clarice Lispector (Atualizado)"}'

# Deletar autor
curl -X DELETE http://127.0.0.1:8000/api/autores/1/
```

### Opção 3: Usar o Postman (Recomendado)
1. Importe a coleção Postman fornecida
2. Execute os testes pré-configurados
3. Veja responses em JSON formatado

### Opção 4: Usar Python Requests

```python
import requests
import json

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
print(response.status_code)
```

---

## RESPOSTAS ESPERADAS

### Sucesso (Lista)
```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "nome": "Machado de Assis"
    }
  ]
}
```

### Sucesso (Detalhe)
```json
{
  "id": 1,
  "nome": "Machado de Assis"
}
```

### Erro (Validação)
```json
{
  "nome": [
    "Este campo é obrigatório."
  ]
}
```

### Erro (Não Encontrado)
```json
{
  "detail": "Não encontrado."
}
```

---

## FILTROS DISPONÍVEIS

- **search**: Busca por nome (Autores/Editoras) ou título/ISBN (Livros)
- **ordering**: Ordena por campos específicos
- **page**: Paginação (padrão: 10 itens por página)

Exemplo:
```
GET /api/autores/?search=Machado&ordering=nome&page=1
```

---

## RECURSOS ADICIONAIS

- 📘 [Django REST Framework - Documentação](https://www.django-rest-framework.org/)
- 📘 [Browse API do DRF](http://127.0.0.1:8000/api/)
- 📘 [Admin Django](http://127.0.0.1:8000/admin/)

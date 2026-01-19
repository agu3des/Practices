#!/usr/bin/env python
"""
EXEMPLOS PRÁTICOS - Como usar a API REST da Biblioteca
Copie e cole os exemplos para testar!
"""

"""
═════════════════════════════════════════════════════════════════════════════
                    EXEMPLOS COM REQUESTS (Python)
═════════════════════════════════════════════════════════════════════════════
"""

# Exemplo 1: Listar Autores
"""
import requests

response = requests.get('http://127.0.0.1:8000/api/autores/')
autores = response.json()
print(f"Total de autores: {autores['count']}")
for autor in autores['results']:
    print(f"  - {autor['nome']}")
"""

# Exemplo 2: Criar Novo Autor
"""
import requests

dados = {"nome": "Jorge Amado"}
response = requests.post('http://127.0.0.1:8000/api/autores/', json=dados)

if response.status_code == 201:
    novo_autor = response.json()
    print(f"Autor criado! ID: {novo_autor['id']}, Nome: {novo_autor['nome']}")
else:
    print(f"Erro: {response.status_code}")
    print(response.json())
"""

# Exemplo 3: Buscar Autor Específico
"""
import requests

response = requests.get('http://127.0.0.1:8000/api/autores/1/')
autor = response.json()
print(f"ID: {autor['id']}, Nome: {autor['nome']}")
"""

# Exemplo 4: Atualizar Autor (PUT - Completo)
"""
import requests

dados = {"nome": "Jorge Amado (Atualizado)"}
response = requests.put('http://127.0.0.1:8000/api/autores/1/', json=dados)

if response.status_code == 200:
    autor_atualizado = response.json()
    print(f"Autor atualizado: {autor_atualizado['nome']}")
"""

# Exemplo 5: Atualizar Parcialmente (PATCH)
"""
import requests

dados = {"nome": "Novo Nome"}
response = requests.patch('http://127.0.0.1:8000/api/autores/1/', json=dados)
print(response.json())
"""

# Exemplo 6: Deletar Autor
"""
import requests

response = requests.delete('http://127.0.0.1:8000/api/autores/1/')
if response.status_code == 204:
    print("Autor deletado com sucesso!")
"""

# Exemplo 7: Buscar com Filtro (search)
"""
import requests

response = requests.get('http://127.0.0.1:8000/api/autores/?search=Machado')
resultados = response.json()
print(f"Encontrados {resultados['count']} autores")
for autor in resultados['results']:
    print(f"  - {autor['nome']}")
"""

# Exemplo 8: Ordenar Resultados
"""
import requests

# Alfabética A-Z
response = requests.get('http://127.0.0.1:8000/api/autores/?ordering=nome')
print("Autores em ordem alfabética:")

# Alfabética Z-A
response = requests.get('http://127.0.0.1:8000/api/autores/?ordering=-nome')
print("Autores em ordem reversa:")
"""

# Exemplo 9: Paginação
"""
import requests

# Página 1 (padrão: 10 itens)
response = requests.get('http://127.0.0.1:8000/api/autores/?page=1')
dados = response.json()
print(f"Total: {dados['count']} autores")
print(f"Próxima página: {dados['next']}")
print(f"Página anterior: {dados['previous']}")
print(f"Resultados nesta página: {len(dados['results'])}")
"""

# Exemplo 10: Combinar Filtros
"""
import requests

url = 'http://127.0.0.1:8000/api/autores/?search=Machado&ordering=nome&page=1'
response = requests.get(url)
print(response.json())
"""

# Exemplo 11: Criar Editora
"""
import requests

dados = {"nome": "Rocco Editora"}
response = requests.post('http://127.0.0.1:8000/api/editoras/', json=dados)
if response.status_code == 201:
    editora = response.json()
    print(f"Editora criada! ID: {editora['id']}")
"""

# Exemplo 12: Criar Livro
"""
import requests

dados = {
    "ISBN": "9788535914849",
    "titulo": "Capitães da Areia",
    "publicacao": "1937-12-08",
    "preco": "52.90",
    "estoque": 25,
    "editora": 1  # ID da editora
}
response = requests.post('http://127.0.0.1:8000/api/livros/', json=dados)
if response.status_code == 201:
    livro = response.json()
    print(f"Livro criado! ID: {livro['id']}")
    print(f"Título: {livro['titulo']}")
    print(f"Editora: {livro['editora_nome']}")
"""

# Exemplo 13: Vincular Autor a Livro (Publicação)
"""
import requests

dados = {
    "livro": 1,  # ID do livro
    "autor": 1   # ID do autor
}
response = requests.post('http://127.0.0.1:8000/api/publicacoes/', json=dados)
if response.status_code == 201:
    publicacao = response.json()
    print(f"Vínculo criado: {publicacao['livro_titulo']} → {publicacao['autor_nome']}")
"""

# Exemplo 14: Listar com Headers Personalizados
"""
import requests

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'Meu-App-1.0'
}

response = requests.get('http://127.0.0.1:8000/api/autores/', headers=headers)
print(response.json())
"""

# Exemplo 15: Tratamento de Erros
"""
import requests

try:
    response = requests.get('http://127.0.0.1:8000/api/autores/999/')
    response.raise_for_status()  # Lança exceção se status >= 400
except requests.exceptions.HTTPError:
    print(f"Erro HTTP: {response.status_code}")
    print(response.json())
except requests.exceptions.ConnectionError:
    print("Erro de conexão: Servidor não respondeu")
except Exception as e:
    print(f"Erro inesperado: {str(e)}")
"""

"""
═════════════════════════════════════════════════════════════════════════════
                        EXEMPLOS COM cURL (Terminal)
═════════════════════════════════════════════════════════════════════════════
"""

"""
1. Listar Autores
   curl http://127.0.0.1:8000/api/autores/

2. Criar Autor
   curl -X POST http://127.0.0.1:8000/api/autores/ \
     -H "Content-Type: application/json" \
     -d '{"nome":"Paulo Coelho"}'

3. Buscar Autor Específico
   curl http://127.0.0.1:8000/api/autores/1/

4. Atualizar Autor
   curl -X PUT http://127.0.0.1:8000/api/autores/1/ \
     -H "Content-Type: application/json" \
     -d '{"nome":"Paulo Coelho (Atualizado)"}'

5. Atualizar Parcialmente
   curl -X PATCH http://127.0.0.1:8000/api/autores/1/ \
     -H "Content-Type: application/json" \
     -d '{"nome":"Novo Nome"}'

6. Deletar Autor
   curl -X DELETE http://127.0.0.1:8000/api/autores/1/

7. Buscar com Filtro
   curl "http://127.0.0.1:8000/api/autores/?search=Machado"

8. Ordenar
   curl "http://127.0.0.1:8000/api/autores/?ordering=nome"

9. Paginação
   curl "http://127.0.0.1:8000/api/autores/?page=2"

10. Ver Headers de Resposta
    curl -i http://127.0.0.1:8000/api/autores/

11. Ver apenas Headers
    curl -I http://127.0.0.1:8000/api/autores/

12. Salvar Resposta em Arquivo
    curl http://127.0.0.1:8000/api/autores/ > autores.json

13. Com Verbose (mostra detalhes)
    curl -v http://127.0.0.1:8000/api/autores/
"""

"""
═════════════════════════════════════════════════════════════════════════════
                    EXEMPLOS COM JAVASCRIPT/Node.js
═════════════════════════════════════════════════════════════════════════════
"""

"""
// 1. Listar Autores
fetch('http://127.0.0.1:8000/api/autores/')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Erro:', error));

// 2. Criar Autor
fetch('http://127.0.0.1:8000/api/autores/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ nome: 'Paulo Coelho' })
})
  .then(response => response.json())
  .then(data => console.log('Autor criado:', data))
  .catch(error => console.error('Erro:', error));

// 3. Buscar Autor
fetch('http://127.0.0.1:8000/api/autores/1/')
  .then(response => response.json())
  .then(autor => console.log(autor))
  .catch(error => console.error('Erro:', error));

// 4. Atualizar Autor
fetch('http://127.0.0.1:8000/api/autores/1/', {
  method: 'PUT',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ nome: 'Novo Nome' })
})
  .then(response => response.json())
  .then(data => console.log('Atualizado:', data))
  .catch(error => console.error('Erro:', error));

// 5. Deletar Autor
fetch('http://127.0.0.1:8000/api/autores/1/', {
  method: 'DELETE'
})
  .then(response => {
    if (response.status === 204) {
      console.log('Deletado com sucesso');
    }
  })
  .catch(error => console.error('Erro:', error));

// 6. Com async/await
async function listarAutores() {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/autores/');
    const dados = await response.json();
    console.log(dados);
  } catch (error) {
    console.error('Erro:', error);
  }
}

// 7. Com axios (se instalado)
// npm install axios

// Listar
axios.get('http://127.0.0.1:8000/api/autores/')
  .then(res => console.log(res.data))
  .catch(err => console.error(err));

// Criar
axios.post('http://127.0.0.1:8000/api/autores/', {
  nome: 'Paulo Coelho'
})
  .then(res => console.log('Criado:', res.data))
  .catch(err => console.error(err));
"""

"""
═════════════════════════════════════════════════════════════════════════════
                          EXEMPLOS POSTMAN
═════════════════════════════════════════════════════════════════════════════
"""

"""
VARIÁVEIS POSTMAN:
{{base_url}} = http://127.0.0.1:8000/api
{{author_id}} = 1
{{publisher_id}} = 1

1. Listar Autores
   GET {{base_url}}/autores/
   
2. Criar Autor
   POST {{base_url}}/autores/
   Body (raw JSON):
   {
     "nome": "Paulo Coelho"
   }
   
3. Buscar Autor
   GET {{base_url}}/autores/{{author_id}}/
   
4. Atualizar Autor
   PUT {{base_url}}/autores/{{author_id}}/
   Body (raw JSON):
   {
     "nome": "Paulo Coelho (Atualizado)"
   }
   
5. Deletar Autor
   DELETE {{base_url}}/autores/{{author_id}}/

6. Buscar com Filtro
   GET {{base_url}}/autores/?search=Machado
   
7. Ordenar
   GET {{base_url}}/autores/?ordering=nome
   
8. Testar Script
   Depois de criar:
   pm.environment.set("author_id", pm.response.json().id);
"""

"""
═════════════════════════════════════════════════════════════════════════════
                    FLUXO COMPLETO - Criar Livro com Autor
═════════════════════════════════════════════════════════════════════════════
"""

"""
PASSO 1: Criar um Autor
POST /api/autores/
{
  "nome": "Aluísio Azevedo"
}
Resposta: {"id": 1, "nome": "Aluísio Azevedo"}

PASSO 2: Criar uma Editora
POST /api/editoras/
{
  "nome": "Rocco"
}
Resposta: {"id": 1, "nome": "Rocco"}

PASSO 3: Criar um Livro
POST /api/livros/
{
  "ISBN": "9788532526304",
  "titulo": "O Mulato",
  "publicacao": "1881-12-12",
  "preco": "39.90",
  "estoque": 15,
  "editora": 1
}
Resposta: {"id": 1, "titulo": "O Mulato", "editora_nome": "Rocco", ...}

PASSO 4: Vincular Autor ao Livro
POST /api/publicacoes/
{
  "livro": 1,
  "autor": 1
}
Resposta: {"id": 1, "livro_titulo": "O Mulato", "autor_nome": "Aluísio Azevedo"}

PASSO 5: Verificar Livro com Detalhes
GET /api/livros/1/
Resposta mostrará:
{
  "id": 1,
  "titulo": "O Mulato",
  "autores": [
    {"id": 1, "nome": "Aluísio Azevedo"}
  ],
  "editora_nome": "Rocco",
  ...
}
"""

"""
═════════════════════════════════════════════════════════════════════════════
                      CASOS DE ERRO E SOLUÇÕES
═════════════════════════════════════════════════════════════════════════════
"""

"""
ERRO 1: 400 Bad Request - Campo obrigatório faltando
Requisição:
POST /api/autores/
{}

Resposta:
{
  "nome": ["This field is required."]
}

Solução: Adicione o campo "nome"

---

ERRO 2: 400 Bad Request - Campo não único
Requisição:
POST /api/autores/
{
  "nome": "Machado de Assis"  # Já existe
}

Resposta:
{
  "nome": ["This field must be unique."]
}

Solução: Use um nome diferente

---

ERRO 3: 404 Not Found - ID não existe
Requisição:
GET /api/autores/999/

Resposta:
{
  "detail": "Not found."
}

Solução: Verifique o ID correto

---

ERRO 4: 405 Method Not Allowed
Requisição:
PATCH /api/autores/  # Não é permitido em lista

Solução: Use PATCH apenas em detalhes: /api/autores/{id}/

---

ERRO 5: 500 Server Error
Isso significa erro interno do Django. Verifique:
- Se o servidor está rodando
- Se há erros no terminal do Django
- Se o banco de dados está acessível
"""

"""
═════════════════════════════════════════════════════════════════════════════
                    DICAS E BOAS PRÁTICAS
═════════════════════════════════════════════════════════════════════════════
"""

"""
✅ FAÇA:
1. Sempre incluir Content-Type: application/json
2. Validar dados antes de enviar
3. Verificar status codes das respostas
4. Usar IDs corretos para operações
5. Testar com curl antes de usar em aplicação
6. Implementar retry logic para falhas temporárias
7. Logar requisições e respostas para debug
8. Usar variáveis em Postman para reutilização

❌ NÃO FAÇA:
1. Não confiar em dados do cliente
2. Não usar hardcoded IDs
3. Não ignorar erros HTTP
4. Não fazer muitas requisições simultâneas (sem rate limiting)
5. Não expor senhas ou tokens em logs
6. Não fazer operações críticas sem validar
7. Não esquecer de tratar exceções de conexão
8. Não testar em produção diretamente
"""

print("✅ Arquivo de exemplos carregado! Copie e cole os exemplos nos seus projetos.")

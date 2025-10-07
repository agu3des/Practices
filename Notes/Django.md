# Django

Permite criar campos rapidamente apenas arrastando elementos, permite integração com bancos de dados

scaffold → crud completo para alguma coisa

Ver docker!!!!

- Open source em 2005
- Arquitetura baseada no padrão MTV (model-template-view)
    - Model: gerencia os dados e o ORM
    - Template: camada de apresentação (html)
    - View: lógica de negócio e controle → controller

### Criando apps, rotas e views

- Pasta *myapp* com:
    - __init__.py : indica que o diretório corrente deve ser considerado um pacote Python.
    - [asgi.py](http://asgi.py/) : ponto de entrada para servidores web compatíveis com ASGI.
    - [wsgi.py](http://wsgi.py/): ponto de entrada para servidores web compatíveis com WSGI.
    - [urls.py](http://urls.py/): URLs do projeto (rotas).
    - [settings.py](http://settings.py/): configurações do projeto Django.
- db.sqlite3: Banco de Dados Sqlite
- [manage.py](http://manage.py/): utilitário por linha de comando para interagir com o projeto Django. Como exemplo de seu uso, inicializamos o servidor web com ele:

$python manage.py runserver 0.0.0.0:8000

- Comando:

**$** python manage.py startapp polls

- Isso criará um diretório *polls* como mostra a imagem ao lado.
- **migrations/** → histórico de mudanças no banco. Guarda os arquivos de migração.
- **admin.py** → integração com o admin. Usado para registrar os models no Django Admin.
- **apps.py** → configuração do app.
- **models.py** → descreve os *models* do app.
- **tests.py** → testes do app.
- **views.py** → lógica para responder às requisições.

### URL’s

- Como vimos anteriormente, as rotas do projeto são definidas no arquivo **urls.py**.
    - Nele são mapeadas as URLs →Views.
- Usa-se a função *path()* para criar as rotas.
- Pode ser definido em:
    - urls.py do projeto (arquivo principal):
        - Normalmente inclui rotas globais;
        - Pode “delegar” para os apps.
    - urls.py de cada *app*
        - Cada app tem seu próprio mapeamento.

É possível incluir rotas que estão em outros arquivos através da função *include*.

### VIEW’s

- Implementações como funções ou classes em Python
- Recebem uma requisição HTTP e retorna uma resposta também http
- Papel central no padrão MVT (Model-View-Template)
- Estão associadas à URL’s e possuem a lógica do negócio
- Podem ser: Function-Based Views (FBV) ou Class-Based Views (CBV)

```jsx
from django.http import HttpResponse

def hello(request):
	return HttpResponse("Hellho, Django")
```
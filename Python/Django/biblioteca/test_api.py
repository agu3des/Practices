#!/usr/bin/env python
"""
Script de Teste da API REST - Biblioteca
Testa operações CRUD para Autores e Editoras
"""

import requests
import json
from datetime import datetime

# Configuração
API_BASE_URL = "http://127.0.0.1:8000/api"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Cores para output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_section(title):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*70}")
    print(f"{title}")
    print(f"{'='*70}{Colors.ENDC}\n")


def print_success(message):
    print(f"{Colors.OKGREEN}✓ {message}{Colors.ENDC}")


def print_error(message):
    print(f"{Colors.FAIL}✗ {message}{Colors.ENDC}")


def print_info(message):
    print(f"{Colors.OKCYAN}ℹ {message}{Colors.ENDC}")


def print_json(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))


def test_autores():
    """Testa operações CRUD para Autores"""
    print_section("TESTANDO AUTORES - OPERAÇÕES CRUD")
    
    # CREATE - Criar novo autor
    print_info("1. Criando novo autor...")
    autor_data = {"nome": "Machado de Assis"}
    response = requests.post(f"{API_BASE_URL}/autores/", json=autor_data, headers=HEADERS)
    
    if response.status_code == 201:
        print_success(f"Autor criado com sucesso")
        autor = response.json()
        autor_id = autor['id']
        print_json(autor)
    else:
        print_error(f"Erro ao criar autor: {response.status_code}")
        print_json(response.json())
        return
    
    # READ - Listar todos os autores
    print_info("\n2. Listando todos os autores...")
    response = requests.get(f"{API_BASE_URL}/autores/", headers=HEADERS)
    
    if response.status_code == 200:
        print_success("Autores listados com sucesso")
        data = response.json()
        print_info(f"Total de autores: {data.get('count', len(data.get('results', [])))}")
        print_json(data['results'][:3])  # Mostra apenas os 3 primeiros
    else:
        print_error(f"Erro ao listar autores: {response.status_code}")
    
    # READ - Buscar autor específico
    print_info(f"\n3. Buscando autor específico (ID: {autor_id})...")
    response = requests.get(f"{API_BASE_URL}/autores/{autor_id}/", headers=HEADERS)
    
    if response.status_code == 200:
        print_success("Autor encontrado")
        print_json(response.json())
    else:
        print_error(f"Erro ao buscar autor: {response.status_code}")
    
    # UPDATE - Atualizar autor (PUT)
    print_info(f"\n4. Atualizando autor (ID: {autor_id}) - PUT...")
    updated_data = {"nome": "Machado de Assis (Atualizado)"}
    response = requests.put(f"{API_BASE_URL}/autores/{autor_id}/", json=updated_data, headers=HEADERS)
    
    if response.status_code == 200:
        print_success("Autor atualizado com sucesso")
        print_json(response.json())
    else:
        print_error(f"Erro ao atualizar autor: {response.status_code}")
    
    # UPDATE - Atualizar parcialmente (PATCH)
    print_info(f"\n5. Atualizando parcialmente autor (ID: {autor_id}) - PATCH...")
    partial_data = {"nome": "Machado de Assis (Revisado)"}
    response = requests.patch(f"{API_BASE_URL}/autores/{autor_id}/", json=partial_data, headers=HEADERS)
    
    if response.status_code == 200:
        print_success("Autor atualizado parcialmente com sucesso")
        print_json(response.json())
    else:
        print_error(f"Erro ao atualizar autor: {response.status_code}")
    
    # SEARCH - Buscar por nome
    print_info("\n6. Buscando autores por nome (search)...")
    response = requests.get(f"{API_BASE_URL}/autores/?search=Machado", headers=HEADERS)
    
    if response.status_code == 200:
        print_success("Busca realizada com sucesso")
        data = response.json()
        print_info(f"Resultados encontrados: {data.get('count', 0)}")
        print_json(data['results'])
    else:
        print_error(f"Erro na busca: {response.status_code}")
    
    # ORDERING - Ordenar por nome
    print_info("\n7. Ordenando autores por nome...")
    response = requests.get(f"{API_BASE_URL}/autores/?ordering=nome", headers=HEADERS)
    
    if response.status_code == 200:
        print_success("Ordenação realizada com sucesso")
        print_json(response.json()['results'][:5])
    else:
        print_error(f"Erro na ordenação: {response.status_code}")
    
    # DELETE - Deletar autor
    print_info(f"\n8. Deletando autor (ID: {autor_id})...")
    response = requests.delete(f"{API_BASE_URL}/autores/{autor_id}/", headers=HEADERS)
    
    if response.status_code == 204:
        print_success("Autor deletado com sucesso")
    else:
        print_error(f"Erro ao deletar autor: {response.status_code}")
    
    # Verificar se foi deletado
    print_info(f"\n9. Verificando se autor foi deletado...")
    response = requests.get(f"{API_BASE_URL}/autores/{autor_id}/", headers=HEADERS)
    
    if response.status_code == 404:
        print_success("Autor não encontrado (confirmando exclusão)")
    else:
        print_error("Autor ainda existe no banco de dados")


def test_editoras():
    """Testa operações CRUD para Editoras"""
    print_section("TESTANDO EDITORAS - OPERAÇÕES CRUD")
    
    # CREATE - Criar nova editora
    print_info("1. Criando nova editora...")
    editora_data = {"nome": "Companhia das Letras"}
    response = requests.post(f"{API_BASE_URL}/editoras/", json=editora_data, headers=HEADERS)
    
    if response.status_code == 201:
        print_success("Editora criada com sucesso")
        editora = response.json()
        editora_id = editora['id']
        print_json(editora)
    else:
        print_error(f"Erro ao criar editora: {response.status_code}")
        print_json(response.json())
        return
    
    # READ - Listar todas as editoras
    print_info("\n2. Listando todas as editoras...")
    response = requests.get(f"{API_BASE_URL}/editoras/", headers=HEADERS)
    
    if response.status_code == 200:
        print_success("Editoras listadas com sucesso")
        data = response.json()
        print_info(f"Total de editoras: {data.get('count', len(data.get('results', [])))}")
        print_json(data['results'][:3])
    else:
        print_error(f"Erro ao listar editoras: {response.status_code}")
    
    # READ - Buscar editora específica
    print_info(f"\n3. Buscando editora específica (ID: {editora_id})...")
    response = requests.get(f"{API_BASE_URL}/editoras/{editora_id}/", headers=HEADERS)
    
    if response.status_code == 200:
        print_success("Editora encontrada")
        print_json(response.json())
    else:
        print_error(f"Erro ao buscar editora: {response.status_code}")
    
    # UPDATE - Atualizar editora
    print_info(f"\n4. Atualizando editora (ID: {editora_id})...")
    updated_data = {"nome": "Editora Saraiva"}
    response = requests.put(f"{API_BASE_URL}/editoras/{editora_id}/", json=updated_data, headers=HEADERS)
    
    if response.status_code == 200:
        print_success("Editora atualizada com sucesso")
        print_json(response.json())
    else:
        print_error(f"Erro ao atualizar editora: {response.status_code}")
    
    # SEARCH - Buscar por nome
    print_info("\n5. Buscando editoras por nome...")
    response = requests.get(f"{API_BASE_URL}/editoras/?search=Saraiva", headers=HEADERS)
    
    if response.status_code == 200:
        print_success("Busca realizada com sucesso")
        data = response.json()
        print_info(f"Resultados encontrados: {data.get('count', 0)}")
        print_json(data['results'])
    else:
        print_error(f"Erro na busca: {response.status_code}")
    
    # DELETE - Deletar editora
    print_info(f"\n6. Deletando editora (ID: {editora_id})...")
    response = requests.delete(f"{API_BASE_URL}/editoras/{editora_id}/", headers=HEADERS)
    
    if response.status_code == 204:
        print_success("Editora deletada com sucesso")
    else:
        print_error(f"Erro ao deletar editora: {response.status_code}")


def test_livros():
    """Testa operações com Livros"""
    print_section("TESTANDO LIVROS - OPERAÇÕES CRUD")
    
    # Criar uma editora primeiro
    print_info("Criando editora para teste...")
    editora_data = {"nome": "Rocco"}
    response = requests.post(f"{API_BASE_URL}/editoras/", json=editora_data, headers=HEADERS)
    
    if response.status_code != 201:
        print_error("Erro ao criar editora para teste")
        return
    
    editora_id = response.json()['id']
    print_success(f"Editora criada com ID: {editora_id}")
    
    # CREATE - Criar novo livro
    print_info("\n1. Criando novo livro...")
    livro_data = {
        "ISBN": "9788535914849",
        "titulo": "Dom Casmurro",
        "publicacao": "1899-12-31",
        "preco": "45.90",
        "estoque": 10,
        "editora": editora_id
    }
    response = requests.post(f"{API_BASE_URL}/livros/", json=livro_data, headers=HEADERS)
    
    if response.status_code == 201:
        print_success("Livro criado com sucesso")
        livro = response.json()
        livro_id = livro['id']
        print_json(livro)
    else:
        print_error(f"Erro ao criar livro: {response.status_code}")
        print_json(response.json())
        return
    
    # READ - Listar todos os livros
    print_info("\n2. Listando todos os livros...")
    response = requests.get(f"{API_BASE_URL}/livros/", headers=HEADERS)
    
    if response.status_code == 200:
        print_success("Livros listados com sucesso")
        data = response.json()
        print_info(f"Total de livros: {data.get('count', 0)}")
    else:
        print_error(f"Erro ao listar livros: {response.status_code}")
    
    # SEARCH - Buscar por título
    print_info("\n3. Buscando livros por título...")
    response = requests.get(f"{API_BASE_URL}/livros/?search=Dom", headers=HEADERS)
    
    if response.status_code == 200:
        print_success("Busca realizada com sucesso")
        print_json(response.json()['results'])
    else:
        print_error(f"Erro na busca: {response.status_code}")


def test_api_status():
    """Verifica o status geral da API"""
    print_section("STATUS DA API")
    
    endpoints = [
        ("Autores", "/autores/"),
        ("Editoras", "/editoras/"),
        ("Livros", "/livros/"),
        ("Publicações", "/publicacoes/"),
    ]
    
    for name, endpoint in endpoints:
        try:
            response = requests.get(f"{API_BASE_URL}{endpoint}", headers=HEADERS, timeout=5)
            if response.status_code == 200:
                data = response.json()
                count = data.get('count', 0)
                print_success(f"{name}: {count} registros")
            else:
                print_error(f"{name}: Erro {response.status_code}")
        except requests.exceptions.ConnectionError:
            print_error(f"{name}: Servidor não respondeu")
        except Exception as e:
            print_error(f"{name}: Erro - {str(e)}")


def main():
    """Função principal"""
    print(f"\n{Colors.BOLD}{'='*70}")
    print(f"TESTE DA API REST - BIBLIOTECA DJANGO")
    print(f"Versão 1.0 - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"{'='*70}{Colors.ENDC}")
    
    # Verificar status da API
    test_api_status()
    
    # Testar operações CRUD
    test_autores()
    test_editoras()
    test_livros()
    
    print_section("TESTES CONCLUÍDOS")
    print_success("Todos os testes foram executados!")
    print_info("Para mais detalhes, consulte a documentação em API_TESTING_GUIDE.md")
    print(f"\n{Colors.OKBLUE}Endpoints disponíveis:{Colors.ENDC}")
    print("  • GET    /api/autores/           - Listar autores")
    print("  • POST   /api/autores/           - Criar autor")
    print("  • GET    /api/autores/{id}/      - Buscar autor")
    print("  • PUT    /api/autores/{id}/      - Atualizar autor")
    print("  • PATCH  /api/autores/{id}/      - Atualizar parcialmente")
    print("  • DELETE /api/autores/{id}/      - Deletar autor")
    print("  • GET    /api/editoras/          - Listar editoras")
    print("  • POST   /api/editoras/          - Criar editora")
    print("  • GET    /api/editoras/{id}/     - Buscar editora")
    print("  • PUT    /api/editoras/{id}/     - Atualizar editora")
    print("  • DELETE /api/editoras/{id}/     - Deletar editora")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}Testes interrompidos pelo usuário{Colors.ENDC}")
    except Exception as e:
        print(f"\n{Colors.FAIL}Erro durante testes: {str(e)}{Colors.ENDC}")

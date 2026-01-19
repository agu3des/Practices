#!/usr/bin/env bash
# QUICK START - API REST Biblioteca
# Execute este script para começar rapidamente

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║       API REST BIBLIOTECA - QUICK START                       ║"
echo "║       Django REST Framework - CRUD de Autor e Editora         ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Cores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}📦 PASSO 1: Verificando dependências...${NC}"
python -c "import django; print(f'✅ Django {django.VERSION[0]}.{django.VERSION[1]} instalado')" 2>/dev/null || echo "❌ Django não instalado"
python -c "import rest_framework; print(f'✅ Django REST Framework instalado')" 2>/dev/null || echo "⚠️  DRF não instalado. Instalando..."

if ! python -c "import rest_framework" 2>/dev/null; then
    echo -e "${YELLOW}Instalando Django REST Framework...${NC}"
    pip install djangorestframework
    echo -e "${GREEN}✅ DRF instalado!${NC}"
fi

echo ""
echo -e "${BLUE}🔄 PASSO 2: Aplicando migrações...${NC}"
python manage.py migrate
echo -e "${GREEN}✅ Migrações aplicadas!${NC}"

echo ""
echo -e "${BLUE}🚀 PASSO 3: Iniciando servidor...${NC}"
echo -e "${YELLOW}O servidor será iniciado em: http://127.0.0.1:8000/${NC}"
echo ""
echo -e "${GREEN}Acesse no navegador:${NC}"
echo -e "  📍 Raiz: http://127.0.0.1:8000/"
echo -e "  📍 API: http://127.0.0.1:8000/api/"
echo -e "  📍 Autores: http://127.0.0.1:8000/api/autores/"
echo -e "  📍 Editoras: http://127.0.0.1:8000/api/editoras/"
echo ""
echo -e "${YELLOW}Para parar o servidor, pressione: CTRL+C${NC}"
echo ""

python manage.py runserver

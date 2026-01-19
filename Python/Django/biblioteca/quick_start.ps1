# QUICK START - API REST Biblioteca (Windows PowerShell)
# Execute este script para começar rapidamente

Write-Host "╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║       API REST BIBLIOTECA - QUICK START                       ║" -ForegroundColor Cyan
Write-Host "║       Django REST Framework - CRUD de Autor e Editora         ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Passo 1: Verificar dependências
Write-Host "📦 PASSO 1: Verificando dependências..." -ForegroundColor Blue

try {
    $django = python -c "import django; print(f'Django {django.VERSION[0]}.{django.VERSION[1]}')" 2>$null
    Write-Host "✅ $django instalado" -ForegroundColor Green
} catch {
    Write-Host "❌ Django não instalado" -ForegroundColor Red
    exit
}

try {
    python -c "import rest_framework" 2>$null
    Write-Host "✅ Django REST Framework instalado" -ForegroundColor Green
} catch {
    Write-Host "⚠️  DRF não instalado. Instalando..." -ForegroundColor Yellow
    pip install djangorestframework
    Write-Host "✅ DRF instalado!" -ForegroundColor Green
}

Write-Host ""
Write-Host "🔄 PASSO 2: Aplicando migrações..." -ForegroundColor Blue
python manage.py migrate
Write-Host "✅ Migrações aplicadas!" -ForegroundColor Green

Write-Host ""
Write-Host "🚀 PASSO 3: Iniciando servidor..." -ForegroundColor Blue
Write-Host ""
Write-Host "O servidor será iniciado em: http://127.0.0.1:8000/" -ForegroundColor Yellow
Write-Host ""
Write-Host "Acesse no navegador:" -ForegroundColor Green
Write-Host "  📍 Raiz: http://127.0.0.1:8000/" -ForegroundColor Cyan
Write-Host "  📍 API: http://127.0.0.1:8000/api/" -ForegroundColor Cyan
Write-Host "  📍 Autores: http://127.0.0.1:8000/api/autores/" -ForegroundColor Cyan
Write-Host "  📍 Editoras: http://127.0.0.1:8000/api/editoras/" -ForegroundColor Cyan
Write-Host ""
Write-Host "Para parar o servidor, pressione: CTRL+C" -ForegroundColor Yellow
Write-Host ""

python manage.py runserver

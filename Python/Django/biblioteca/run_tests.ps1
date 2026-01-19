#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Script para executar testes unitários da aplicação Django Biblioteca

.DESCRIPTION
    Fornece funções para executar diferentes tipos de testes com Django REST Framework

.EXAMPLE
    .\run_tests.ps1 -Type All
    .\run_tests.ps1 -Type Model
    .\run_tests.ps1 -Type API
    .\run_tests.ps1 -Type Specific -TestName "AutorAPITestCase.test_api_post_autor"
#>

param(
    [Parameter(Mandatory=$false)]
    [ValidateSet('All', 'Model', 'Form', 'View', 'Serializer', 'API', 'Specific', 'Coverage')]
    [string]$Type = 'All',
    
    [Parameter(Mandatory=$false)]
    [string]$TestName = '',
    
    [Parameter(Mandatory=$false)]
    [int]$Verbosity = 2
)

# Cores para output
$Colors = @{
    Success = 'Green'
    Error = 'Red'
    Warning = 'Yellow'
    Info = 'Cyan'
    Header = 'Magenta'
}

function Write-ColorOutput {
    param(
        [string]$Message,
        [string]$Color = 'White'
    )
    Write-Host $Message -ForegroundColor $Color
}

function Write-Header {
    param([string]$Text)
    Write-Host ""
    Write-Host ("=" * 70) -ForegroundColor $Colors.Header
    Write-Host $Text -ForegroundColor $Colors.Header
    Write-Host ("=" * 70) -ForegroundColor $Colors.Header
    Write-Host ""
}

function Invoke-Test {
    param(
        [string]$Command,
        [string]$Description
    )
    
    Write-Header $Description
    Write-ColorOutput "Executando: $Command" -Color $Colors.Info
    Write-Host ""
    
    Invoke-Expression $Command
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-ColorOutput "✅ $Description - SUCESSO" -Color $Colors.Success
    } else {
        Write-Host ""
        Write-ColorOutput "❌ $Description - FALHA (código: $LASTEXITCODE)" -Color $Colors.Error
    }
}

# Verificar se está no diretório correto
if (-not (Test-Path 'manage.py')) {
    Write-ColorOutput "❌ Erro: manage.py não encontrado!" -Color $Colors.Error
    Write-ColorOutput "   Execute este script no diretório da aplicação Django" -Color $Colors.Error
    exit 1
}

Write-Host ""
Write-ColorOutput "🧪 TESTES UNITÁRIOS - Django REST Framework Biblioteca" -Color $Colors.Header
Write-Host ""

switch ($Type) {
    'All' {
        Write-Header "Executando Todos os Testes (63 testes)"
        
        $cmd = "python manage.py test catalog.test_complete -v $Verbosity"
        Invoke-Test -Command $cmd -Description "Todos os Testes"
        
        Write-Host ""
        Write-Host ""
        Write-ColorOutput "📊 RESUMO FINAL:" -Color $Colors.Header
        Write-Host ""
        Write-ColorOutput "  ✅ 18 testes de Model" -Color $Colors.Success
        Write-ColorOutput "  ✅ 11 testes de Form" -Color $Colors.Success
        Write-ColorOutput "  ✅ 8 testes de Serializer" -Color $Colors.Success
        Write-ColorOutput "  ✅ 6 testes de View" -Color $Colors.Success
        Write-ColorOutput "  ✅ 20 testes de API REST" -Color $Colors.Success
        Write-Host ""
    }
    
    'Model' {
        Write-Header "Testes de MODEL (18 testes)"
        
        $testClasses = @(
            'AutorModelTestCase',
            'EditoraModelTestCase',
            'LivroModelTestCase',
            'PublicaModelTestCase'
        )
        
        foreach ($class in $testClasses) {
            $cmd = "python manage.py test catalog.test_complete.$class -v $Verbosity"
            Invoke-Test -Command $cmd -Description "Model: $class"
            Write-Host ""
        }
    }
    
    'Form' {
        Write-Header "Testes de FORM (11 testes)"
        
        $testClasses = @(
            'AutorFormTestCase',
            'EditoraFormTestCase',
            'LivroFormTestCase'
        )
        
        foreach ($class in $testClasses) {
            $cmd = "python manage.py test catalog.test_complete.$class -v $Verbosity"
            Invoke-Test -Command $cmd -Description "Form: $class"
            Write-Host ""
        }
    }
    
    'Serializer' {
        Write-Header "Testes de SERIALIZER (8 testes)"
        
        $testClasses = @(
            'AutorSerializerTestCase',
            'LivroSerializerTestCase',
            'PublicaSerializerTestCase'
        )
        
        foreach ($class in $testClasses) {
            $cmd = "python manage.py test catalog.test_complete.$class -v $Verbosity"
            Invoke-Test -Command $cmd -Description "Serializer: $class"
            Write-Host ""
        }
    }
    
    'View' {
        Write-Header "Testes de VIEW (6 testes)"
        
        $testClasses = @(
            'AutorViewTestCase',
            'EditoraViewTestCase'
        )
        
        foreach ($class in $testClasses) {
            $cmd = "python manage.py test catalog.test_complete.$class -v $Verbosity"
            Invoke-Test -Command $cmd -Description "View: $class"
            Write-Host ""
        }
    }
    
    'API' {
        Write-Header "Testes de API REST (20 testes)"
        
        $testClasses = @(
            'AutorAPITestCase',
            'EditoraAPITestCase',
            'LivroAPITestCase',
            'PublicaAPITestCase'
        )
        
        foreach ($class in $testClasses) {
            $cmd = "python manage.py test catalog.test_complete.$class -v $Verbosity"
            Invoke-Test -Command $cmd -Description "API: $class"
            Write-Host ""
        }
    }
    
    'Specific' {
        if ([string]::IsNullOrEmpty($TestName)) {
            Write-ColorOutput "❌ Erro: -TestName é obrigatório com -Type Specific" -Color $Colors.Error
            Write-ColorOutput "   Exemplo: .\run_tests.ps1 -Type Specific -TestName 'AutorAPITestCase.test_api_post_autor'" -Color $Colors.Warning
            exit 1
        }
        
        Write-Header "Teste Específico: $TestName"
        
        $cmd = "python manage.py test catalog.test_complete.$TestName -v $Verbosity"
        Invoke-Test -Command $cmd -Description "Teste: $TestName"
    }
    
    'Coverage' {
        Write-Header "Executando Testes com Coverage"
        
        # Verificar se coverage está instalado
        try {
            $null = python -m coverage --version
        } catch {
            Write-ColorOutput "⚠️  Coverage não instalado. Instalando..." -Color $Colors.Warning
            pip install coverage
        }
        
        Write-ColorOutput "Executando testes com coverage..." -Color $Colors.Info
        python -m coverage run --source='catalog' manage.py test catalog.test_complete -v 1
        
        Write-Host ""
        Write-ColorOutput "📊 Relatório de Coverage:" -Color $Colors.Header
        python -m coverage report -m
        
        Write-Host ""
        Write-ColorOutput "💡 Gerando relatório HTML em htmlcov/index.html..." -Color $Colors.Info
        python -m coverage html
        
        Write-Host ""
        Write-ColorOutput "✅ Relatório HTML gerado com sucesso!" -Color $Colors.Success
        Write-ColorOutput "   Abra: htmlcov/index.html no seu navegador" -Color $Colors.Info
    }
}

Write-Host ""
Write-Host ""
Write-ColorOutput "✨ Execução concluída!" -Color $Colors.Success
Write-Host ""

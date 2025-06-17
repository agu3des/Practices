# Registros encontrados no arquivo
def registros(file: str) -> list:
    arq = open(file, 'r')
    lista = arq.read().splitlines()
    arq.close()
    # A primeira linha contém o cabeçalho de cada campo.
    # Retornar a partir da segunda linha
    return lista[1:]

# Quantidade de registros
def quantidade_registros(registros: list) -> int:
    return len(registros)

# Relação dos Campi da Instituição.
def campi(registros: list) -> list:
    pass

# Relação dos Cursos de um determinado Campus.
def cursos(registros: list, nome_campus: str) -> list:
    pass

# Maior nota da instituição
def maior_nota_instituicao(registros: list) -> float:
    pass

# Maior nota do Campus
def maior_nota_campus(registros: list, nome_campus: str) -> float:
    pass

# Maior nota de um Curso
def maior_nota_curso(registros: list, codigo_curso: int) -> float:
    pass

# Maior nota de corte da instituição
def maior_nota_corte_instituicao(registros: list) -> float:
    pass

# Maior nota do Campus
def maior_nota_corte_campus(registros: list, nome_campus: str) -> float:
    pass

# Maior nota de um Curso
def maior_nota_corte_curso(registros: list, codigo_curso: int) -> float:
    pass

# Retorna o código de um determinado curso de um determinado campus
def codigo_curso(registros: list, nome_campus: str, nome_curso: str) -> int:
    pass
class DisciplinaRepositorio {
    constructor() {
        this.disciplinas = [];
        this.alunosPorDisciplina = [];  
    }

    inserir(disciplina) {
        this.disciplinas.push(disciplina);  
    }

    remover(codigo) {
        const indxDisciplinaARemover = this.disciplinas.findIndex(disciplina => disciplina.codigo === codigo);
        if (indxDisciplinaARemover > -1) {
            this.disciplinas.splice(indxDisciplinaARemover, 1);
            delete this.alunosPorDisciplina[codigo]; 
        } else {
            throw new Error('Disciplina não encontrada!');
        }
    }

    listar() {
        return this.disciplinas;
    }

    inserirAlunoNaDisciplina(aluno, codigoDisciplina) {
        this.alunosPorDisciplina.push(`${aluno}+${codigoDisciplina}`);
    }
}

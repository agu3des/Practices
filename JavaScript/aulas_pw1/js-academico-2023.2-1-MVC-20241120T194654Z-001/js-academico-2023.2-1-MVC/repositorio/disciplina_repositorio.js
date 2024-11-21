class DisciplinaRepositorio {
    
    constructor() {
        this.disciplinas = [];
        this.alunos = [];
    }

    inserir(disciplina) {
        this.disciplinas.push(disciplina);
    }

    remover(codigo) {
        const indxDisciplinaARemover = this.disciplinas.findIndex(disciplina => disciplina.codigo === codigo);

        if(indxDisciplinaARemover > -1) {
            this.disciplinas.splice(indxDisciplinaARemover, 1);
        }
    }

    listar() {
        return this.disciplinas;
    }

    
    inserirAlunoNaDisciplina(aluno) {
        this.alunos.push(aluno);
    }

 /*   atualizar(codigo, novoCodigo, novoNome) {
        
        const disciplina =  this.repositorio.listar().filter(disciplina => disciplina.codigo === codigo); 
        const disciplinaAntiga = disciplina;

        setCodigo(novoCodigo);
        disciplina.setNome(novoNome);

        this.inserir(disciplina);
        this.remover(disciplinaAntiga);
    }
*/

}
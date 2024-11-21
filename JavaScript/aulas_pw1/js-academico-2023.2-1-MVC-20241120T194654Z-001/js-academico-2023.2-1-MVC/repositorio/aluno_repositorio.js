class AlunoRepositorio {

    constructor() {
        this.alunos = [];
    }

    inserir(aluno) {
        this.alunos.push(aluno);
    }

    remover(matricula) {
        const indxAlunoARemover = this.alunos.findIndex(aluno => aluno.matricula === matricula);
        if (indxAlunoARemover > -1) {
            this.alunos.splice(indxAlunoARemover, 1);
        } else {
            throw new Error('Aluno não encontrado!');
        }
    }

    listar() {
        return this.alunos;
    }
}

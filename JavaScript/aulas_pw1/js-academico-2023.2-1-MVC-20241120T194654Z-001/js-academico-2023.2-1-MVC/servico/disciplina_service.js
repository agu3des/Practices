import 'modelo/aluno.js';

class DisciplinaService {
    constructor() {
        this.repositorio = new DisciplinaRepositorio();
    }

    inserir(codigo, nome) {
        const disciplinaPesquisada = this.pesquisarPorCodigo(codigo);

        if(disciplinaPesquisada.length > 0) {
            throw new Error('Disciplina já existe!');
        }

        const disciplinaNova = new Disciplina(codigo, nome);
        this.repositorio.inserir(disciplinaNova);
        return disciplinaNova;
    }

    pesquisarPorCodigo(codigo) {
        return this.repositorio.listar().filter(disciplina => disciplina.codigo === codigo); 
    }

    remover(codigo) {
        this.repositorio.remover(codigo);
    }

    inserirAlunoNaDisciplina(nome, idade, matricula, disciplina) {
        const aluno = new Aluno()
    }
}
//import Aluno from './modelo/aluno.js';

class DisciplinaService {
    constructor() {
        this.repositorio = new DisciplinaRepositorio();
    }

    inserir(codigo, nome) {

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

    inserirAlunoNaDisciplina(aluno, disciplina) {
        const disciplinaEncontrada = this.pesquisarPorCodigo(disciplina.codigo);
        if (!disciplinaEncontrada) {
            throw new Error('Disciplina não encontrada!');
        }
        this.repositorio.inserirAlunoNaDisciplina(aluno); 
    }
}

//import Aluno from './modelo/aluno.js';

class DisciplinaService {
    constructor() {
        this.repositorio = new DisciplinaRepositorio();
    }

    inserir(codigo, nome) {
        const disciplinaPesquisada = this.pesquisarPorCodigo(codigo);

        if (disciplinaPesquisada.length > 0) {
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

    inserirAlunoNaDisciplina(nome, idade, matricula, codigoDisciplina) {
        const aluno = new Aluno(nome, idade, matricula);
        const disciplinasEncontradas = this.pesquisarPorCodigo(codigoDisciplina);

        if (disciplinasEncontradas.length > 0) {
            const disciplina = disciplinasEncontradas[0];  
            this.repositorio.inserirAlunoNaDisciplina(aluno);
            return aluno;  
        } else {
            throw new Error('Disciplina não encontrada!');
        }
    }
}
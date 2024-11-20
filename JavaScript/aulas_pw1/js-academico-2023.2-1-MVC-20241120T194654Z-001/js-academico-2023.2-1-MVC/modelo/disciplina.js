class Disciplina {
    
    constructor(codigo, nome) {
        this._codigo = codigo;
        this._nome = nome;
        this._alunos = [];
    }

    get codigo() {
        return this._codigo;
    }

    get nome() {
        return this._nome;
    }

    set setCodigo(novoCodigo) {
        this._codigo = novoCodigo;
    }

    set setNome(novoNome) {
        this._nome = novoNome;
    }
}
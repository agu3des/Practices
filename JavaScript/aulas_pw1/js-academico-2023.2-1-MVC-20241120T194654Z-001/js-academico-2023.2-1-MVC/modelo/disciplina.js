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

    set codigo(novoCodigo) {
        this._codigo = novoCodigo;
    }

    set nome(novoNome) {
        this._nome = novoNome;
    }
}
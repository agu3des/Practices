//1. Desenvolver a classe Cliente, contendo como atributos: nome, cpf e uma conta (apenas para simplificar), e seus respectivos métodos get e set;
class Cliente {
    constructor(nome, cpf, conta) {
        this._nome = nome;
        this._cpf = cpf;
        this._conta = conta;
    }
    get nome() {
        return this._nome;
    }
    set nome(novoNome) {
        this._nome = novoNome;
    }
    get cpf() {
        return this._cpf;
    }
    set cpf(novoCpf) {
        this._cpf = novoCpf;
    }
    get conta() {
        return this._conta;
    }
    set conta(novaConta) {
        this._conta = novaConta;
    }
    toString() {
        return `Nome: ${this._nome}\nCpf: ${this._cpf}\nConta: ${this._conta}`;
    }
}

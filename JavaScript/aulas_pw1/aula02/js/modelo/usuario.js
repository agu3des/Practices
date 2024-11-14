class Usuario {
    constructor(nome, idade, cpf) {
        this._nome = nome;
        this._idade = idade; //alterar algo já existente
        this.cpf = cpf //this._cpf = cpf  por conta do _ ele entende que é algo privado apenas para o dev - mas é uma convenção
    }

    get nome() { //não posso colocar _nome aqui, pois o get não pode ter o mesmo nome, pois ele fará recursão, a função chamará a si própria
        return this.nome; //se tivesse _ no nome eu teria que colocar this._nome
    }

    set nome(novoNome) {
        this.nome = novoNome; //u1.nome = 'Gustavo' parece que eu estou alterando o atributo mas é a função, ele passa esse valor atribuído como parâmetro
    }

    get idade() {
        return this._idade;
    }

    set idade(novaIdade) {
        if (novaIdade < 0) {
            throw new Error('Idade inválida');
        }
        this._idade = novaIdade;

    }

}
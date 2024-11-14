class RepositorioUsuario {
    constructor() {
        this.usuarios = [];
    }

        inserir(usuario) {
            this.usuarios.push(usuario);
        }

        remover(cpf) {
            const indxusuarioARemover = this.usuarios.indexOf(usuario => usuario.cpf === cpf); //a mesma coisa de fazer um for
            this.usuarios.splice(indxusuarioARemover, 1); //o número diz quanto eu quero remover , nesse caso só 1 ent só o próprio, remove a posição e atualiza a lista ou seja n fica undefind lá
        }

        buscarPorCpf(cpf) {
            return this.usuarios.filter(usuario => usuario.cpf === cpf);
        }

        buscarPorNome(nome) {
            return this.usuarios.filter(usuario => usuario.nome === nome);
        }
}
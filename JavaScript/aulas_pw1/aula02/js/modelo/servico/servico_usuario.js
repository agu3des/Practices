//regras de negócio

class UsuarioServiço {
    constructor() {
        this.repositorio = new RepositorioUsuario();
    }

    inserir(nome, idade, cpf) {
        this.validarIdade(idade);
        this.validarCpf(cpf);

        const usuarioAInserir = new Usuario(nome, idade, cpf);
        this.repositorio.inserir(usuarioAInserir);
    }

    remover(cpf) {
        this.repositorio.remover(cpf);
    }

    listar() {
        return this.repositorio.usuarios;
    }

    validarIdade(idade) {
        if (idade < 0 ) {
            throw new Error('Idade inválida');
        }
    }

    validadeCpf(cpf) {
        if (cpf.length != 11) {
            throw new Error('CPF inválido');
        }
        const usuarioBuscado = this.repositorio.buscarPorCpf(cpf);
        if (usuarioBuscado) {
            throw new Error('Usuário já cadastrado');
        }
    
    }




}
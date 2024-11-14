class ControladorUsuario {
    constructor() {
        this.servico = new UsuarioServico();
    }
    inserir() {
        const inputUsuarioNome = document.querySelector('#nome');
        const inputUsuarioIdade = document.querySelector('#idade');
        const inputUsuarioCpf = document.querySelector('#cpf');
        try{
            this.servico.inserir(inputUsuarioNome.value, inputUsuarioIdade.value, inputUsuarioCpf.value);
        } catch (e) {
            alert(e);
        }
    }
 




}
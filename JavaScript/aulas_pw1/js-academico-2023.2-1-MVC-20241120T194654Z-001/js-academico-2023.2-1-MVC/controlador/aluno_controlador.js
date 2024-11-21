class AlunoControlador {

    constructor() {
        this.servico = new AlunoService();
    }

    inserir() {
        const nomeElemento = document.querySelector("#nome");
        const idadeElemento = document.querySelector("#idade");
        const matriculoElemento = document.querySelector("#matricula");
        
        try {
            const alunoInserido = this.servico.inserir(nomeElemento.value, Number(idadeElemento.value),
                matriculoElemento.value);
            const listaAlunosElemento = document.querySelector("#listaAlunos");
            if (alunoInserido) {
                this.inserirAlunoNoHtml(alunoInserido, listaAlunosElemento);
            }
        } catch (error) {
            this.exibirMensagemDeErro(error.message);
        }
    }

    inserirAlunoNoHtml(aluno, elementoDestino) {
        const alunoElemento = document.createElement("li");
        alunoElemento.textContent = `Nome: ${aluno.nome} - Idade: ${aluno.idade}`;
        elementoDestino.appendChild(alunoElemento);
    }

    listarAlunosMenoresIdade() {
        const listaAlunosMenoresElemento = document.querySelector('#listaAlunosMenores');
        const alunosMenores = this.servico.listarMenoresIdade();
        alunosMenores.forEach(menor => this.inserirAlunoNoHtml(menor, listaAlunosMenoresElemento));
    }

    exibirMensagemDeErro(mensagem) {
        const erroElemento = document.createElement("p");
        erroElemento.style.color = "red";
        erroElemento.textContent = `Erro: ${mensagem}`;
        document.body.appendChild(erroElemento);
    }
}
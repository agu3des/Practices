class DisciplinaControlador {

    constructor() {
        this.servico = new DisciplinaService();
    }

    inserir() {
        const codigoElemento = document.querySelector("#codigo");
        const nomeElemento = document.querySelector("#nome");
        
        try {
            const disciplinaInserida = this.servico.inserir(codigoElemento.value, nomeElemento.value);
            const listaDisciplinasElemento = document.querySelector("#listaDisciplinas");
            if (disciplinaInserida) {
                this.inserirDisciplinaNoHtml(disciplinaInserida, listaDisciplinasElemento);
            }
        } catch (error) {
            this.exibirMensagemDeErro(error.message);
        }
    }

    inserirDisciplinaNoHtml(disciplina, elementoDestino) {
        const disciplinaElemento = document.createElement("li");
        disciplinaElemento.textContent = `Código: ${disciplina.codigo} - Nome: ${disciplina.nome}`;
        elementoDestino.appendChild(disciplinaElemento);
    }

    inserirAlunoNaDisciplina() {
        const nomeElemento = document.querySelector("#nomeAluno");
        const idadeElemento = document.querySelector("#idadeAluno");
        const matriculoElemento = document.querySelector("#matriculaAluno");
        const disciplinaElementoA = document.querySelector("#disciplina");

        try {
            this.servico.inserirAlunoNaDisciplina(nomeElemento.value, Number(idadeElemento.value), matriculoElemento.value, disciplinaElementoA.value);
        } catch (error) {
            this.exibirMensagemDeErro(error.message);
        }
    }

    exibirMensagemDeErro(mensagem) {
        const erroElemento = document.createElement("p");
        erroElemento.style.color = "red";
        erroElemento.textContent = `Erro: ${mensagem}`;
        document.body.appendChild(erroElemento);
    }
}
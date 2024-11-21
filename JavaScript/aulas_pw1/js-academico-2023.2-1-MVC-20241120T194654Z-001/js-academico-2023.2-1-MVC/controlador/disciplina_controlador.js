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
        const matriculaElemento = document.querySelector("#matriculaAluno");
        const disciplinaElementoA = document.querySelector("#disciplina");

        try {
            if (!nomeElemento.value || !idadeElemento.value || !matriculaElemento.value || !disciplinaElementoA.value) {
                throw new Error("Todos os campos devem ser preenchidos corretamente.");
            }

            const aluno = new Aluno(nomeElemento.value, Number(idadeElemento.value), matriculaElemento.value);
            const disciplina = this.servico.pesquisarPorCodigo(disciplinaElementoA.value);

            if (!disciplina || disciplina.length === 0) {
                throw new Error("Disciplina não encontrada!");
            }

            this.servico.inserirAlunoNaDisciplina(aluno, disciplina);

            this.exibirAlunoNaDisciplina(aluno, disciplina);

        } catch (error) {
            this.exibirMensagemDeErro(error.message);
        }
    }

    exibirAlunoNaDisciplina(aluno, disciplina) {
        const elementoDestino = document.querySelector("#listaAlunos");
        const alunoElemento = document.createElement("li");
        alunoElemento.textContent = `Aluno: ${aluno.nome} - Matrícula: ${aluno.matricula} - Disciplina: ${disciplina.nome}`;
        elementoDestino.appendChild(alunoElemento);
    }

    exibirMensagemDeErro(mensagem) {
        const erroElemento = document.createElement("p");
        erroElemento.style.color = "red";
        erroElemento.textContent = `Erro: ${mensagem}`;
        document.body.appendChild(erroElemento);
    }
}

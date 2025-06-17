package pdm.sistemaacademico

import java.time.LocalDate
import java.util.Scanner

// -------------------- SISTEMA --------------------
class SistemaAcademico {
    private val alunos = mutableListOf<Pessoa>()
    private val scanner = Scanner(System.`in`)

    fun menu() {
        while (true) {
            println(
                """
                ---- MENU ----
                1. Adicionar aluno
                2. Adicionar mestrando
                3. Inserir notas
                4. Verificar situações
                5. Listar alunos
                6. Sair
                Escolha: 
            """.trimIndent()
            )
            when (scanner.nextLine().toIntOrNull()) {
                1 -> adicionarAluno()
                2 -> adicionarMestrando()
                3 -> inserirNotas()
                4 -> verificarSituacoes()
                5 -> listarAlunos()
                6 -> return
                else -> println("Opção inválida.")
            }
        }
    }

    private fun adicionarAluno() {
        println("Nome:")
        val nome = scanner.nextLine()
        println("CPF:")
        val cpf = scanner.nextLine()
        println("Data de nascimento (yyyy-mm-dd):")
        val nascimento = LocalDate.parse(scanner.nextLine())
        println("Matrícula:")
        val matricula = scanner.nextLine().toInt()

        alunos.add(Aluno(nome, cpf, nascimento, matricula))
    }

    private fun adicionarMestrando() {
        println("Nome:")
        val nome = scanner.nextLine()
        println("CPF:")
        val cpf = scanner.nextLine()
        println("Data de nascimento (yyyy-mm-dd):")
        val nascimento = LocalDate.parse(scanner.nextLine())
        println("Matrícula:")
        val matricula = scanner.nextLine().toInt()
        println("Tema da dissertação:")
        val tema = scanner.nextLine()

        alunos.add(AlunoMestrado(nome, cpf, nascimento, matricula, tema))
    }

    private fun inserirNotas() {
        val aluno = selecionarAluno() as? Aluno ?: return
        println("Digite até 3 notas:")
        repeat(3) {
            print("Nota ${it + 1}: ")
            aluno.adicionarNota(scanner.nextLine().toDoubleOrNull() ?: 0.0)
        }

        if (aluno.situacao == "Final") {
            print("Nota de recuperação: ")
            aluno.adicionarNotaRecuperacao(scanner.nextLine().toDoubleOrNull() ?: 0.0)
        }
    }

    private fun verificarSituacoes() {
        for (pessoa in alunos) {
            println("--------")
            pessoa.apresentar()
            if (pessoa is Aluno) {
                pessoa.mostrarNotas()
                val resultado = pessoa.obterResultado()
                println("Média: %.2f | Situação: %s".format(resultado.media, resultado.situacao))
            }
        }
    }

    private fun listarAlunos() {
        alunos.forEachIndexed { i, a -> println("${i + 1}. ${a.nome}") }
    }

    private fun selecionarAluno(): Pessoa? {
        listarAlunos()
        print("Escolha o número do aluno: ")
        val i = scanner.nextLine().toIntOrNull()
        return if (i != null && i in 1..alunos.size) alunos[i - 1] else null
    }
}

// -------------------- MAIN --------------------
fun main() {
    val sistema = SistemaAcademico()
    sistema.menu()
}
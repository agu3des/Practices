package pdm.sistemaacademico

import java.time.LocalDate
import java.time.Period

// -------------------- CLASSE BASE ALUNO --------------------
open class Aluno(
    nome: String,
    cpf: String,
    dataNascimento: LocalDate,
    val matricula: Int
) : Pessoa(nome, cpf, dataNascimento) {

    protected val notas = mutableListOf<Double>()
    protected var notaRecuperacao: Double? = null

    override fun apresentar() {
        println("Aluno: $nome | Matrícula: $matricula | Idade: $idade | CPF: $cpf")
    }

    fun adicionarNota(nota: Double) {
        if (nota in 0.0..10.0 && notas.size < 3) {
            notas.add(nota)
        }
    }

    fun adicionarNotaRecuperacao(nota: Double) {
        if (nota in 0.0..10.0) {
            notaRecuperacao = nota
        }
    }

    val mediaFinal: Double
        get() = if (notaRecuperacao != null) {
            (notas.average() + notaRecuperacao!!) / 2
        } else notas.average()

    val situacao: String
        get() = when {
            mediaFinal >= 7.0 -> "Aprovado"
            mediaFinal >= 4.0 && notaRecuperacao == null -> "Final"
            mediaFinal >= 5.0 && notaRecuperacao != null -> "Aprovado após Final"
            else -> "Reprovado"
        }

    fun obterResultado(): Resultado = Resultado(mediaFinal, situacao)

    fun mostrarNotas() {
        println("Notas: ${notas.joinToString(", ")}")
        notaRecuperacao?.let { println("Recuperação: $it") }
    }

    // Companion Object
    companion object {
        const val NUMERO_MAXIMO_NOTAS = 3

        fun criarAluno(nome: String, cpf: String, dataNascimento: LocalDate, matricula: Int): Aluno {
            return Aluno(nome, cpf, dataNascimento, matricula)
        }

        // Função para calcular a idade com base na data de nascimento
        fun calcularIdade(dataNascimento: LocalDate, dataAtual: LocalDate = LocalDate.now()): Int {
            return Period.between(dataNascimento, dataAtual).years
        }
    }
}

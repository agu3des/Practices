package pdm.sistemaacademico

import java.time.LocalDate

// -------------------- SUBCLASSE COM POLIMORFISMO --------------------
class AlunoMestrado(
    nome: String,
    cpf: String,
    dataNascimento: LocalDate,
    matricula: Int,
    val tema: String
) : Aluno(nome, cpf, dataNascimento, matricula) {

    override fun apresentar() {
        println("Mestrando: $nome | Tema: \"$tema\" | Matrícula: $matricula")
    }
}
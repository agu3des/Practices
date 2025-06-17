package pdm.sistemaacademico

import java.time.LocalDate
import java.time.Period

// -------------------- ABSTRACT CLASS --------------------
abstract class Pessoa(
    val nome: String,
    val cpf: String,
    val dataNascimento: LocalDate
) {
    val idade: Int
        get() = Period.between(dataNascimento, LocalDate.now()).years

    abstract fun apresentar()
}
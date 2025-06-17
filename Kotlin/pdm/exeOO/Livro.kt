package pdm.exeOO

import java.time.LocalDate

class Livro (val titulo: String, val autor: String, val anoPublicacao: Int) {

    init{
        if (anoPublicacao > LocalDate.now().year) {
            throw IllegalArgumentException("Ano com valor inválido!")
        }
    }

    constructor(titulo:String, autor: String) : this(titulo, autor, anoPublicacao = 2025)

    fun imprimirLivro() {
        println("Título: $titulo | Autor: $autor | Ano de Publicação: $anoPublicacao" )
    }

}

fun main(){
    val l1:Livro = Livro("A morte de Ivan Ilitch", "Tolstoi", 1912);
    l1.imprimirLivro();
    val l2:Livro = Livro("Como eu era antes de você", "Nicholas Sparks");
    l2.imprimirLivro();
    val l3:Livro = Livro("É assim que acaba", "Collen Hover", 2026);
    l3.imprimirLivro();
}


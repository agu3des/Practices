package pdm.exeOO

abstract class Funcionario(val nome:String, var salarioBase:Double) {

    open fun salarioTotal() {
        println("Salário do funcionário $nome é $salarioBase")
    }

}


class Gerente(nome:String, salarioBase:Double, val bonus:Double): Funcionario(nome, salarioBase) {

    override fun salarioTotal() {
        salarioBase += bonus
        println("Salário do funcionário $nome é $salarioBase")
    }

    fun exibirInfo() {
        println("Nome: $nome | Salário Base: $salarioBase")
    }
}




fun main(){
    val f1 = Gerente("Ivan Ilitch", 1912.17, 25.68);
    f1.salarioTotal();
    f1.exibirInfo();
    val g2 = Gerente("Nicholas Sparks", 1583.37, 359.74);
    g2.salarioTotal();
    g2.exibirInfo();

}
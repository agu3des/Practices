package pdm.exeOO

class ContaBancaria (val numero:Int, val titular:String, var saldo:Double){

    init{
        counter++;
    }

    fun depositar(valor:Double){
        if(valor <= 0) {
            throw IllegalArgumentException("Valor inválido!")
        } else {
            saldo += valor;
        }

    }
    fun sacar(valor:Double) {
        if(valor > saldo) {
            throw IllegalArgumentException("Valor inválido, saldo insuficiente!")
        } else {
            saldo -= valor;
        }

    }

    companion object {
        private var counter = 0
    }

    fun qtdContas(){
        println("A quantidade de contas já criadas é: $counter.")
    }

    fun imprimeConta(){
        println("Conta: $numero | Titular: $titular | Saldo: $saldo")
    }
    /*
    override fun toString(): String {
        return  "Conta: $numero | Titular: $titular | Saldo: $saldo"
    }
    */

}

fun main(){
    val c1:ContaBancaria = ContaBancaria(123, "Tolstoi", 1912.00);
    c1.depositar(1.00);
    c1.imprimeConta();
    val c2:ContaBancaria = ContaBancaria(459, "Nicholas Sparks", 4359.45);
    c2.sacar(359.45);
    c2.imprimeConta();
    val c3:ContaBancaria = ContaBancaria(678, "Collen Hover", 2026.83);
    //c3.sacar(2027.00);
    c3.imprimeConta();
    c1.qtdContas();
}


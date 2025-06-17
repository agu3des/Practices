package pdm.exeOO

open class Veiculo(val marca:String, val modelo:String) {

    open fun exibirInfo() {
        println("Marca: $marca | Modelo: $modelo")
    }

}


class Carro(marca:String, modelo:String, val qtdPortas:Int) : Veiculo(marca, modelo) {

    override fun exibirInfo(){
        println("Marca: $marca | Modelo: $modelo | Qtd de Portas: $qtdPortas")
    }

}

fun exibirDados(veiculo: Veiculo) {
    println(veiculo.exibirInfo())
}


fun main(){
    val c1:Carro = Carro("Fiat", "Uno", 2);
    c1.exibirInfo();
    val c2:Carro = Carro("Byd", "Dolphin", 4);
    c2.exibirInfo();


    val v3:Veiculo = Veiculo("Monark", "Huston");
    v3.exibirInfo();
    val v4:Veiculo = Veiculo("Honda", "Pop");
    v4.exibirInfo();

    exibirDados(v3);
    exibirDados(c2);


}

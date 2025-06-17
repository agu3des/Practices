package pdm.exeOO

import java.awt.geom.Arc2D

interface FormaGeometrica {
    fun area() : Double;

}

class Retangulo(var base:Double, var altura:Double) : FormaGeometrica {
    override fun area(): Double {
        return base*altura;
    }

}

class Triangulo(var base:Double, var altura:Double) : FormaGeometrica {
    override fun area(): Double {
        return (base*altura)/2;
    }

}

class Circulo(var raio:Double) : FormaGeometrica {
    override fun area(): Double {
        return Math.PI * Math.pow(raio,2.0);
    }

}

fun main(){
    val listaDeFiguras = ArrayList<FormaGeometrica>();
    for (i in 1 .. 2) {
        listaDeFiguras.add(Retangulo( (i + 1).toDouble(), (i*2).toDouble() ) );
    }

    for (i in 1 .. 2) {
        listaDeFiguras.add(Triangulo( (i + 1).toDouble(), (i*2).toDouble() ) );
    }

    for (i in 1 .. 2) {
        listaDeFiguras.add(Circulo( (i + 1).toDouble() ) );
    }

    for (figura in listaDeFiguras) {
        println(figura.area());
    }
}
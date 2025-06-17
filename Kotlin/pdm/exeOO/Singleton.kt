package pdm.exeOO

class Singleton private constructor() {
    companion object {
        private val mySingleton = Singleton();
        fun getInstance() = mySingleton;
    }

}
fun main(args: ArrayList<String>) {

}
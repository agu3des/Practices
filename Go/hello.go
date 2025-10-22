package main //so the main function can be called from the package

import "fmt"
//package level declaration
var num0 int = 5 //you have to use this type of declaration

//var name string = "Ananda"
//var surname string = "Guedes"

//CamelCase
var (
	id float32 = 1
	//short variable -> used for a short time
	name string = "Ananda"
	surname string = "Guedes"
)

var A int = 21 //could be acess by any packge if it was a couldn't = global level

func main() {
	//fmt.Println("Hello, World!")

	//function/scolpe level declaration
	var num01 int //declaration
	num01 = 10 //inicialization
	//good for use after

	var num02 float32 = 15 //both in one line
//	var num02 float32 = "hello" it's not goig to work because of the type given
	
	num03 := 20
	//good when you want the golang to inicialize and define a type by itself

	fmt.Println("num01 =", num01)
	fmt.Println("num02 =", num02)
	fmt.Println("num02 =", num03)

	fmt.Printf("%T, %v", num0,num0) //type and value

	fmt.Println(id, name, surname) 



}
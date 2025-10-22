package main

select {
	case v := <- ch :
		fmt . Println ( v )
	case v := <- ch2 :
		fmt . Println ( v )
	case ch3 <- x :
		fmt . Println (" Escreveu ",x )
	case <- ch4
		fmt . Println (" Obteve valor de ch4 , mas ignorou ele ")
}
for {
	select {
		case <- done :
			return
		case v := <- ch :
			fmt.Println ( v )
		case v := <- ch2 :
			fmt.Println ( v )
		case ch3 <- x :
			fmt.Println (" Escreveu ",x)
		case <- ch4
			fmt.Println (" Obteve valor de ch4 , mas ignorou ele ")
		default :
			fmt.Println (" nada a fazer ")
	}
}
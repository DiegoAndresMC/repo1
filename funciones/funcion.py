def saludo(): # def palabra reservada para funciones
	print("Hola")
saludo()

def saludo_params(nombre):#despues del nombre de la funcion va el parametro por el cual se psan valores de fuera de la funcion hacia ella
	var = "Hola " + nombre# se declara variable y concatena el parametro
	print(var)
saludo_params("Diego")#se invoca la funcion y se declara el parametro en cuestion a mostrar por nombre

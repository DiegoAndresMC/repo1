from opera import * #con el * se importan todas las funciones del archivo,
                   #si solo se necesita una se declara cual se necesita
from clase.fuera import * #para importar de otra carpeta es nombre carpeta . mas nombre 
                          #de archivo luego se crea en la otra carpeta __init__.py 
                          #para quye se pueda exportar

res_suma = suma()
print(f"El Resulatdo es: {res_suma}")

res_resta = resta()
print("El Resulatdo es: ",res_resta)

res_valor = saludar()
print("Hola",res_valor)
number1=int(input("Ingresa un numero:"))
number2=int(input("Ingresa otro numero:"))


eleccion = 0

while eleccion != 6:
    print ("""
    Indique la operacion a realizar:
    1) Suma
    2) Resta
    3) Multiplicaion 
    4) Division
    5) Cambiar Valores
    6) Salir
    """) 
    
    eleccion = int(input())
    
    
    if eleccion == 1:
        print(" ")
        print("Resultado: ", number1,"+", number2,"=", number1+number2)

    if eleccion == 2:
        print(" ")
        print("Resultado: ", number1,"-", number2,"=", number1-number2)  

    if eleccion == 3:
        print(" ")
        print("Resultado: ", number1,"*", number2,"=", number1*number2)

    if eleccion == 4:
        print(" ")
        print("Resultado: ", number1,"/", number2,"=", number1/number2)

    if eleccion == 5:
        number1=int(input("Ingresa un numero:"))
        number2=int(input("Ingresa otro numero:"))

    if eleccion == 6:
        print("Gracias por usar la calculadora")

    

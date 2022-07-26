DOLARLEMPIRA = 24.59
def cambiarLempiras(lempiras):
    dolares = lempiras * DOLARLEMPIRA
    return dolares 
def cambiarDolares(dolares):
    lempiras = dolares / DOLARLEMPIRA
    return lempiras
def solicitarCantidad(tipo):
    cantidad = float(input(f"Ingrese Monto de {tipo} a cambiar"))
    return cantidad 

if __name__ == '__main__':
    menu = """ 
    Convertidor de Monedas
    Selecciona la Moneda 
    1) Cambio a Dolares
    2) Cambio a Lempiras 
    3) Salir
    """


    while True:
        opcion = int(input(menu))
        if opcion == 1:
            cantidad = solicitarCantidad("lempiras")
            dolares = round(cambiarLempiras(cantidad),2)
            print(f"El cambio de {cantidad} lempiras es de {dolares} dolares") 
        elif opcion == 2:
            cantidad = solicitarCantidad("dolares")
            lempiras = round(cambiarDolares(cantidad),2)
            print(f"El cambio de {cantidad} dolares es de {lempiras} lempiras")
        else:
            print("Gracias!")
            break 



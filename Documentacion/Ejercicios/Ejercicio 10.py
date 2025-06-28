def main():
    #recibir un numero
    numero_ingresado = int( input("Ingresar el numero a evaluar por favor:") )
    #evaluar si es par
    #imprimir el resultado

    
    if numero_ingresado % 2 == 0 :
        print(f"El {numero_ingresado} SI es PAR")
    else:
        print(f"El {numero_ingresado} NO es PAR")
    
    
main()

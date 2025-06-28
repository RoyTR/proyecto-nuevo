def main():
    #dado 2 numeros
    primer_numero = float( input("Ingrese el primer numero: ") )
    segundo_numero = int( input("Ingrese el segundo numero: ") )
    
    
    #input => texto => "10.5"
    #int ("10.5") => 10
    
    
    #evaluar cual es mayor, menor o iguales
    if primer_numero == segundo_numero :
        print("Ambos numeros son iguales")
    #else:
        #print("Ambos numeros NO son iguales")
    elif primer_numero > segundo_numero :
        print(f"El numero mayor es {primer_numero} y el menor es {segundo_numero}")
    elif primer_numero < segundo_numero :
        print(f"El numero mayor es {segundo_numero} y el menor es {primer_numero}")
    
    #imprimir la respuesta
    
    
main()

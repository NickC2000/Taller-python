def caracteres(palabra):

    primerCaracter = palabra[0]
    ultimoCaracter = palabra[len(palabra) - 1]
    return(primerCaracter,ultimoCaracter)

def main():

    palabra = input("Introduzca una palabra: ")
    (caracterUno,caracterDos) = caracteres(palabra)
    print("Primer caracter: ",caracterUno)
    print("Ultimo caracter: ",caracterDos)

if __name__ == '__main__':
    main()
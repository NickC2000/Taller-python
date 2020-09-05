def edad2070(edad,año):

    diferencia = 2070 - año
    return(diferencia+edad)

def main():

    edad = int(input("Introduzca su edad: "))
    año = int(input("Introduzca el año actual: "))
    print(edad2070(edad,año))

if __name__ == '__main__':
    main()
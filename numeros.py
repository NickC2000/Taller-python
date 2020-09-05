def par_o_impar(numero):

    if numero % 2 == 0:
        return True
    else:
        return False

def main():

    numero = int(input("Introduzca un numero entero: "))
    print("Número par" if par_o_impar(numero) is True else "Número impar")

if __name__ == '__main__':
    main()
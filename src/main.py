from person import Autor

def main()->None:
    nombre = input("Digite el nombre del autor:")
    cedula = int(input("Digite el numero de cedula:"))
    
    autor = Autor(nombre, cedula)
    print(autor)

if __name__ == '__main__':
    main()



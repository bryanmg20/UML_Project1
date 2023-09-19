from person import Autor
from book import Libro, LibroDigital, LibroDigital, LibroImpreso, AudioLibro
def main()->None:
    libro_1 = LibroImpreso(
        titulo = "cien",
        isbn = "3",
        genero ="drama",
        formato ="tapa dura",
        valor = 60000,
        paginas = 100,
        num_ejemplares = 5
    )
    libro_2 = LibroDigital(
        titulo = "hola",
        isbn = "3",
        genero ="drama",
        formato ="pdf",
        valor = 60000,
        has_hipervinculo=True
    )
    libro_3 = AudioLibro(
        titulo = "hola",
        isbn = "3",
        genero ="drama",
        formato ="mp3",
        valor = 60000,
        duracion=330
    )
    print(libro_1)
    print(libro_2)
    print(libro_3)

if __name__ == '__main__':
    main()



from poblacion import *

def test_lee_poblaciones(datos):
    print("***Test de poblaciones***")
    print(f"Se ha leído {len(datos)} registros.")
    print("Mostrando los tres primeros registros:")
    for d in datos[:3]:
        print(d)
    print("Mostrando los tres últimos registros:")
    for d in datos[-3:]:
        print(d)

def test_calcula_paises(datos):
    print("Test calcula países")
    paises_ordenador = calcula_paises(datos)
    for pais in paises_ordenador:
        print(pais)

def test_filtra_por_pais(datos):
    print("Test filtra por país")
    pais = input("Di un país (en inglés) o código: ")
    lista_filtrada = filtra_por_pais(datos, pais)
    for año, censo in lista_filtrada:
        print(f"{año}: {censo}")

def test_filtra_por_paises_y_anyo(datos):
    print("Test filtra por paises y año")
    año = int(input("Año: "))
    paises = {"Albania", "China", "Austria"}
    lista_filtrada = filtra_por_paises_y_anyo(datos, año, paises)
    for censo in lista_filtrada:
        print(f"{año}: {censo}")

def test_muestra_evolucion_poblacion(datos):
    print("Test muestra evolución población")
    pais = input("País: ")
    muestra_evolucion_poblacion(datos, pais)

if __name__ == "__main__":
    datos = lee_poblaciones("./proyecto-poblaciones-DML8267/data/population.csv")
    #test_lee_poblaciones(datos)
    #test_calcula_paises(datos)
    #test_filtra_por_pais(datos)
    #test_filtra_por_paises_y_anyo(datos)
    test_muestra_evolucion_poblacion(datos)
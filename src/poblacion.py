from collections import namedtuple
import csv
from matplotlib import pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    res = []
    with open(ruta_fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        for pais, codigo, año, censo in lector:
            año = int(año)
            censo = int(censo)
            tupla = RegistroPoblacion(pais, codigo, año, censo)
            res.append(tupla)
    return res

def calcula_paises(poblaciones):
    conjunto_paises = set()
    for tupla in poblaciones:
        conjunto_paises.add(tupla.pais)
    return sorted(conjunto_paises)

def filtra_por_pais(poblaciones, nombre_o_codigo):
    lista_filtrada = []
    for pais in poblaciones:
        if pais.pais == nombre_o_codigo or pais.codigo == nombre_o_codigo:
            tupla = (pais.año, pais.censo)
            lista_filtrada.append(tupla)
    return lista_filtrada

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    lista_filtrada = []
    for p in poblaciones:
        if p.año == anyo and p.pais in paises:
            tupla = (p.pais, p.censo)
            lista_filtrada.append(tupla)
    return lista_filtrada

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    filtra_por_pais(poblaciones, nombre_o_codigo)
    lista_años = []
    lista_habitantes = []
    lista_filtrada = filtra_por_pais(poblaciones, nombre_o_codigo)
    for año, censo in lista_filtrada:
        lista_años.append(año)
        lista_habitantes.append(censo)
    plt.title(f"Evolución de la población para {nombre_o_codigo}")
    plt.bar(lista_años, lista_habitantes)
    plt.show()

def muestra_evolucion_paises_anyo(poblaciones, nombre_o_codigo):
    filtra_por_pais(poblaciones, nombre_o_codigo)
    lista_paises = []
    lista_habitantes = []
    lista_filtrada = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    for pais, censo in lista_filtrada:
        lista_paises.append(pais)
        lista_habitantes.append(censo)
    plt.title(f"Evolución de la población para {paises} en el año {anyo}")
    plt.bar(lista_paises, lista_habitantes)
    plt.show()
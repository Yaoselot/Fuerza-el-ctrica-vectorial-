import math
import numpy as np

EPSILON_0 = 8.8541878176e-12
CONSTANTE_COULUMB = 1 / (4 * math.pi * EPSILON_0)

def fuerza_escalar(carga_uno, carga_dos, r):
    c1_x_c2 = carga_uno * carga_dos
    cargas_entre_distancia2 = c1_x_c2 / (r ** 2)
    f = CONSTANTE_COULUMB * cargas_entre_distancia2
    return f

def fuerza_vectorial (carga_uno, carga_dos, vec_uno, vec_dos):
    vec_relativo = vec_dos - vec_uno
    r = np.linalg.norm(vec_relativo) # funcion que calcula la norma del vector, en este caso del vector relativo
    f_coulumb = fuerza_escalar(carga_uno, carga_dos, r) # Calculamos la fuerza de coulumb sin el elemento vectorial aún
    print(f"La fuerza escalar es: {f_coulumb}")
    # Calculamos la fuerza vectorial
    vec_unitario = vec_relativo / r # Encontramos el vector unitario de nuestro vector
    f_vectorial = f_coulumb * vec_unitario # Multiplicamos la fuerza de coulumb con su vector unitario para encontrar la fuerza de coulumb vectorial
    return f_vectorial

input_uno = input("Introduce la primera carga 'ae-n x, y, z': ")
input_dos = input("Introduce la segunda carga 'ae-n x, y, z': ")

separar = input_uno.split(" ", 1)

carga_user_uno = float(separar[0])
vector_user_uno = np.array([int(x) for x in separar[1].split(",")])

separar = input_dos.split(" ", 1)
carga_user_dos = float(separar[0])
vector_user_dos = np.array([int(x) for x in separar[1].split(",")])

print("Muy bien analicemos los datos")
print(f"Carga 1: {carga_user_uno}, vector: {vector_user_uno}")
print(f"Carga 2: {carga_user_dos}, vector: {vector_user_dos}")


resultado = fuerza_vectorial(carga_user_uno, carga_user_dos, vector_user_uno, vector_user_dos)
print(f"La fuerza vectorial es : {resultado} = [{resultado[0]:.2e} {resultado[1]:.2e} {resultado[2]:.2e}]")
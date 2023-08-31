import math as mt
import numpy as np

def sumacomplejos(A, B):
    real, imaginario = A[0] + B[0], A[1] + B[1]
    return real, imaginario
def multiplicacion(A, B):
    real, imaginario = A[0] * B[0] - A[1] * B[1], A[0] * B[1] + A[1] * B[0]
    return real, imaginario
def resta(A, B):
    real, imaginario = A[0] - B[0], A[1] - B[1]
    return real, imaginario
def division(A, B):
    divisonr = ((B[0]) ** 2 + (B[1] ** 2))
    real = (A[0] * B[0] + A[1] * B[1]) / divisonr
    imaginario = (B[0] * A[1] - A[0] * B[1]) / divisonr
    return real, imaginario
def conjudado(A):
    return A[0], A[1] * -1
def modulo(A):
    return (A[0] ** 2 + A[1] ** 2) ** (1 / 2)

def fase(A):
    return mt.atan2(A[1], A[0])
def polar(A):
    return (modulo(A), fase(A))
def complejo(A):
    return A[0]*mt.cos(A[1]), A[0]*mt.sin(A[1])

def sumvectores(A,B):
    tam = int(len(A))
    vect = np.ones(tam, dtype = tuple)
    for i in range(tam):
        vect[i] = sumacomplejos(A[i], B[i])
    return vect
def inversocomplejo(A):
    real, imaginario = int(A[0])*-1, int(A[1])*-1
    return real, imaginario
def inversoaditivovec(A):
    tam = int(len(A))
    for i in range(tam):
        A[i] = inversocomplejo(A[i])
    return A
def escalarmulvec(A,B):
    tam = int(len(B))
    vect = np.ones(tam, dtype=tuple)
    for i in range(tam):
        vect[i] = multiplicacion(A,B[i])
    return vect
def adicionmatrices(A,B):
    filas = len(A)
    columnas = len(A[0])
    mat = np.zeros((filas, columnas), dtype= tuple)
    for j in range(filas):
        for k in range(columnas):
            mat[j][k] = sumacomplejos(A[j][k],B[j][k])
    return mat
def inversomatriz(A):
    filas = len(A)
    col = len(A[0])
    for j in range(filas):
        for k in range(col):
            A[j][k] = (inversocomplejo(A[j][k]))
    return A
def matrizporescalar(A,B):
    filas = len(B)
    col = len(B[0])
    mat = np.ones((filas, col), dtype=tuple)
    if len(A) > 1:
        for j in range(filas):
            for k in range(col):
                mat[j][k] = multiplicacion(A, B[j][k])
        return mat
def transpuesta(A):
    fil = int(len(A))
    col = int(len(A[0]))
    mat = np.zeros((col,fil), dtype = tuple)
    for j in range(col):
        for k in range(fil):
            mat[j][k] = A[k][j]
    return mat
def conjugadavecmat(A):

    try:
        fil = (len(A))
        col = len(A[0])
        for j in range(fil):
            for k in range(col):
                A[j][k] = conjudado(A[j][k])
        return A
    except:
        fil = int(len(A))
        for j in range(fil):
            A[j] = conjudado(A[j])
        return A


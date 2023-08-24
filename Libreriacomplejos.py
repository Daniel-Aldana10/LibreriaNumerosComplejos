import math as mt
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

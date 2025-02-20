import numpy as np
from sympy import Matrix

def InversaClave(clave, abecedario):
    try:
        return np.array(Matrix(clave).inv_mod(len(abecedario)))
    except ValueError:
        raise ValueError("La clave no tiene inversa en módulo len(abecedario), elige otra.")

def ConvertirTexto(entrada, abecedario, a_num=True):
    if a_num:
        return [abecedario.index(letra) for letra in entrada if letra in abecedario]
    return ''.join(abecedario[i % len(abecedario)] for i in entrada)

def FormatearTexto(mensaje, abecedario, tam):
    mensaje = mensaje.upper().replace(' ', '')
    mensaje = ''.join([letra for letra in mensaje if letra in abecedario])
    while len(mensaje) % tam != 0:
        mensaje += 'X'
    return mensaje

def CrearMatriz(datos, tam):
    if len(datos) % tam != 0:
        raise ValueError("El mensaje no está correctamente ajustado.")
    return np.array(datos).reshape(-1, tam)

def Cifrar(mensaje, clave, abecedario):
    tam = clave.shape[0]
    mensaje = FormatearTexto(mensaje, abecedario, tam)
    valores = ConvertirTexto(mensaje, abecedario)
    bloques = CrearMatriz(valores, tam)
    cifrado = np.dot(bloques, clave) % len(abecedario)
    return ConvertirTexto(cifrado.flatten(), abecedario, a_num=False)

def Descifrar(mensaje_cifrado, clave, abecedario):
    tam = clave.shape[0]
    clave_inversa = InversaClave(clave, abecedario)
    valores = ConvertirTexto(mensaje_cifrado, abecedario)
    bloques = CrearMatriz(valores, tam)
    descifrado = np.dot(bloques, clave_inversa) % len(abecedario)
    return ConvertirTexto(descifrado.flatten(), abecedario, a_num=False)

abecedario = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
clave = np.array([[1, 2, 3], [0, 4, 5], [1, 0, 6]])

entrada = "SEGURIDAD Y CIFRADO AVANZADO"

cifrado = Cifrar(entrada, clave, abecedario)
print("Texto cifrado:", cifrado)

descifrado = Descifrar(cifrado, clave, abecedario)
print("Texto descifrado:", descifrado)

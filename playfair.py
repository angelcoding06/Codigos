
abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
              "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def GenerarMatriz(clave, abecedario):
    tabla = [[0 for _ in range(5)] for _ in range(5)]
    referencia = {}
    clave = clave.upper()
    fila, col = 0, 0

    for letra in clave + ''.join(abecedario):
        if letra in referencia:
            continue
        tabla[fila][col] = letra
        if letra in ["I", "J"]:
            referencia["I"] = referencia["J"] = {"fila": fila, "col": col}
        else:
            referencia[letra] = {"fila": fila, "col": col}
        col = 0 if col == 4 else col + 1
        fila += 1 if col == 0 else 0

    return tabla, referencia

def ProcesarTexto(texto):
    texto = texto.upper().replace(" ", "")
    resultado = ""
    i = 0
    while i < len(texto):
        par = texto[i:i+2]
        if len(par) == 1:
            par += "X"
            i += 1
        elif par[0] == par[1]:
            par = par[0] + "X"
        else:
            i += 2
        resultado += par
    return resultado

def CifrarPlayfair(mensaje, tabla, referencia):
    mensaje = ProcesarTexto(mensaje)
    cifrado = ""

    for i in range(0, len(mensaje), 2):
        f1, c1 = referencia[mensaje[i]]["fila"], referencia[mensaje[i]]["col"]
        f2, c2 = referencia[mensaje[i+1]]["fila"], referencia[mensaje[i+1]]["col"]

        if f1 == f2:
            cifrado += tabla[f1][(c1 + 1) % 5] + tabla[f2][(c2 + 1) % 5]
        elif c1 == c2:
            cifrado += tabla[(f1 + 1) % 5][c1] + tabla[(f2 + 1) % 5][c2]
        else:
            cifrado += tabla[f1][c2] + tabla[f2][c1]

    return cifrado

def DescifrarPlayfair(mensaje, tabla, referencia):
    mensaje = ProcesarTexto(mensaje)
    descifrado = ""

    for i in range(0, len(mensaje), 2):
        f1, c1 = referencia[mensaje[i]]["fila"], referencia[mensaje[i]]["col"]
        f2, c2 = referencia[mensaje[i+1]]["fila"], referencia[mensaje[i+1]]["col"]

        if f1 == f2:
            descifrado += tabla[f1][(c1 - 1) % 5] + tabla[f2][(c2 - 1) % 5]
        elif c1 == c2:
            descifrado += tabla[(f1 - 1) % 5][c1] + tabla[(f2 - 1) % 5][c2]
        else:
            descifrado += tabla[f1][c2] + tabla[f2][c1]

    return descifrado

clave = "ClaveSecreta"
tabla, referencia = GenerarMatriz(clave, abecedario)

mensaje_original = "CIFRADO SEGURO"
mensaje_cifrado = CifrarPlayfair(mensaje_original, tabla, referencia)
mensaje_descifrado = DescifrarPlayfair(mensaje_cifrado, tabla, referencia)

print("Texto cifrado:", mensaje_cifrado)
print("Texto descifrado:", mensaje_descifrado)

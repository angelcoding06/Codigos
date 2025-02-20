def cifrar_descifrar(texto, key, alphabet, modo="cifrar"):
    resultado = ""
    desplazamiento = key if modo == "cifrar" else -key

    for letra in texto:
        try:
            index = alphabet.index(letra)
            nuevo_index = (index + desplazamiento) % len(alphabet)
            resultado += alphabet[nuevo_index]
        except ValueError:
            resultado += letra 

    return resultado



alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ!#%$%!&  "
texto_original = "!Co!midita ri?ca!!!"
clave =12

texto_cifrado = cifrar_descifrar(texto_original, clave, alfabeto, "cifrar")
print("Cifrado:", texto_cifrado)

texto_descifrado = cifrar_descifrar(texto_cifrado, clave, alfabeto, "descifrar")
print("Descifrado:", texto_descifrado)

import string
from collections import Counter

frecuencias_esp = {
    'E': 12.7, 'A': 9.0, 'O': 8.4, 'S': 7.9, 'R': 6.7,
    'N': 6.7, 'I': 6.2, 'L': 5.9, 'T': 5.6, 'C': 4.8,
    'U': 4.5, 'D': 4.3, 'P': 3.8, 'B': 3.2, 'V': 2.9,
    'Y': 2.5, 'G': 2.3, 'H': 2.1, 'F': 1.7, 'M': 1.5,
    'Q': 1.1, 'Z': 1.0, 'J': 0.5, 'Ñ': 0.3, 'X': 0.2,
    'K': 0.1, 'W': 0.1
}

frecuencias_eng = {
    'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0,
    'N': 6.7, 'S': 6.3, 'R': 6.0, 'H': 5.9, 'D': 4.3,
    'L': 4.0, 'C': 3.4, 'U': 2.8, 'M': 2.4, 'F': 2.2,
    'P': 2.0, 'G': 2.0, 'B': 1.5, 'Y': 1.0, 'V': 1.0,
    'K': 0.8, 'J': 0.2, 'X': 0.2, 'Q': 0.1, 'Z': 0.1,
    'W': 0.1
}

def contar_frecuencia(texto):
    texto = texto.replace(" ", "").upper()
    contador = Counter(texto)
    total_letras = sum(contador.values())
    frecuencias = {letra: count / total_letras * 100 for letra, count in contador.items()}
    return frecuencias

def descifrar_por_frecuencia(texto, idioma="es"):
    if idioma == "es":
        frecuencias_idioma = frecuencias_esp
    elif idioma == "en":
        frecuencias_idioma = frecuencias_eng
    else:
        raise ValueError("Idioma no soportado. Usa 'es' para español o 'en' para inglés.")
    
    frecuencias_texto = contar_frecuencia(texto)
    letras_frecuentes_texto = sorted(frecuencias_texto.items(), key=lambda item: item[1], reverse=True)
    letras_frecuentes_idioma = sorted(frecuencias_idioma.items(), key=lambda item: item[1], reverse=True)
    
    mapeo_frecuencias = {}
    for i, (letra_texto, _) in enumerate(letras_frecuentes_texto):
        if i < len(letras_frecuentes_idioma):
            letra_idioma = letras_frecuentes_idioma[i][0]
            mapeo_frecuencias[letra_texto] = letra_idioma
    
    texto_descifrado = []
    for letra in texto.upper():
        if letra in mapeo_frecuencias:
            texto_descifrado.append(mapeo_frecuencias[letra])
        else:
            texto_descifrado.append(letra)
    
    return ''.join(texto_descifrado)

mensaje = "ZEBRAS EN LA PLAYA"
mensaje_cifrado = "ZEBRAS EN LA PLAYA"

mensaje_descifrado_es = descifrar_por_frecuencia(mensaje_cifrado, idioma="es")
mensaje_descifrado_en = descifrar_por_frecuencia(mensaje_cifrado, idioma="en")

print("Mensaje original:", mensaje)
print("Mensaje cifrado:", mensaje_cifrado)
print("Mensaje descifrado (Español):", mensaje_descifrado_es)
print("Mensaje descifrado (Inglés):", mensaje_descifrado_en)

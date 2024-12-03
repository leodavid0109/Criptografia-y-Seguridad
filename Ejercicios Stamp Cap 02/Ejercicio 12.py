import ast

import matplotlib.pyplot as plt
from collections import Counter


def contador_frecuencias(texto_cifrado):
    frecuencias_ingles = {
        'A': 8.000395, 'B': 1.535701, 'C': 2.575785, 'D': 4.317924, 'E': 12.575645,
        'F': 2.350463, 'G': 1.982677, 'H': 6.236609, 'I': 6.920007, 'J': 0.145188,
        'K': 0.739906, 'L': 4.057231, 'M': 2.560994, 'N': 6.903785, 'O': 7.591270,
        'P': 1.795742, 'Q': 0.117571, 'R': 5.959034, 'S': 6.340880, 'T': 9.085226,
        'U': 2.841783, 'V': 0.981717, 'W': 2.224893, 'X': 0.179556, 'Y': 1.900888,
        'Z': 0.079130
    }

    def contar_ngramas(texto, n):
        ngramas = [texto[i:i + n] for i in range(len(texto) - n + 1)]
        ngramas_frecuencia = Counter(ngramas)
        return ngramas_frecuencia

    # Hallar las frecuencias de las letras
    frecuencias_letras = contar_ngramas(texto_cifrado, 1)

    # Calcular la frecuencia de las letras en el texto cifrado
    frecuencias_letras = dict(sorted(frecuencias_letras.items()))
    frecuencias_letras = {k: v / len(texto_cifrado) * 100 for k, v in frecuencias_letras.items()}
    frecuencias_letras = dict(sorted(frecuencias_letras.items()))

    # Plotear las frecuencias de las letras en el texto cifrado
    plt.figure(figsize=(10, 5))
    plt.bar(frecuencias_letras.keys(), frecuencias_letras.values())
    plt.xlabel('Letras')
    plt.ylabel('Frecuencia (%)')
    plt.title('Frecuencia de las letras en el texto cifrado')
    plt.show()

    # Definir función que imprima en orden descendente n frecuencias del texto cifrado y del idioma inglés
    def imprimir_frecuencias(frecuencias_texto, frecuencias_idioma, n):
        # Ordenar las frecuencias del texto cifrado
        frecuencias_texto = sorted(frecuencias_texto.items(), key=lambda item: item[1], reverse=True)[:n]
        # Ordenar las frecuencias del idioma inglés
        frecuencias_idioma = sorted(frecuencias_idioma.items(), key=lambda item: item[1], reverse=True)[:n]

        print(f"{'Texto Cifrado':<15} {'Frecuencia (%)':<25} {'Idioma':<15} {'Frecuencia (%)'}")
        print('-' * 75)

        for i in range(min(n, len(frecuencias_texto), len(frecuencias_idioma))):
            textocrifrado, textocifrado_frec = frecuencias_texto[i]
            textoingles, textoingles_frec = frecuencias_idioma[i]

            print(f"{textocrifrado:<15} {textocifrado_frec:<25.2f} {textoingles:<15} {textoingles_frec}")

    print('Frecuencias de las letras en el texto cifrado y en el idioma inglés:')
    # Imprimir las frecuencias de las letras en el texto cifrado y en el idioma inglés
    imprimir_frecuencias(frecuencias_letras, frecuencias_ingles, 26)

    # Hallar las frecuencias de los bigramas
    bigrams_ingles = {
        'TH': 3.882543, 'HE': 3.681391, 'IN': 2.283899, 'ER': 2.178042, 'AN': 2.140460,
        'RE': 1.749394, 'ND': 1.571977, 'ON': 1.418244, 'EN': 1.383239, 'AT': 1.335523,
        'OU': 1.285484, 'ED': 1.275779, 'HA': 1.274742, 'TO': 1.169655, 'OR': 1.151094,
        'IT': 1.134891, 'IS': 1.109877, 'HI': 1.092302, 'ES': 1.092301, 'NG': 1.053385
    }

    texto_cifrado_bigrams = contar_ngramas(texto_cifrado, 2)

    # Calcular la frecuencia de los bigramas en el texto cifrado
    texto_cifrado_bigrams = dict(sorted(texto_cifrado_bigrams.items()))
    texto_cifrado_bigrams = {k: v / len(texto_cifrado) * 100 for k, v in texto_cifrado_bigrams.items()}
    texto_cifrado_bigrams = dict(sorted(texto_cifrado_bigrams.items()))

    print()
    print('Frecuencias de los bigramas en el texto cifrado y en el idioma inglés:')
    # Imprimir las frecuencias de los bigramas en el texto cifrado y en el idioma inglés
    imprimir_frecuencias(texto_cifrado_bigrams, bigrams_ingles, 15)

    trigramas_ingles = {
        'THE': 3.508232,
        'AND': 1.593878,
        'ING': 1.147042,
        'HER': 0.822444,
        'HAT': 0.650715,
        'HIS': 0.596748,
        'THA': 0.593593,
        'ERE': 0.560594,
        'FOR': 0.555372,
        'ENT': 0.530771,
        'ION': 0.506454,
        'TER': 0.461099,
        'WAS': 0.460487,
        'YOU': 0.437213,
        'ITH': 0.431250,
        'VER': 0.430732,
        'ALL': 0.422758,
        'WIT': 0.397290,
        'THI': 0.394796,
        'TIO': 0.378058
    }

    texto_cifrado_trigrams = contar_ngramas(texto_cifrado, 3)

    # Calcular la frecuencia de los trigramas en el texto cifrado
    texto_cifrado_trigrams = dict(sorted(texto_cifrado_trigrams.items()))
    texto_cifrado_trigrams = {k: v / len(texto_cifrado) * 100 for k, v in texto_cifrado_trigrams.items()}
    texto_cifrado_trigrams = dict(sorted(texto_cifrado_trigrams.items()))

    print()
    print('Frecuencias de los trigramas en el texto cifrado y en el idioma inglés:')
    # Imprimir las frecuencias de los trigramas en el texto cifrado y en el idioma inglés
    imprimir_frecuencias(texto_cifrado_trigrams, trigramas_ingles, 20)

    # Hallar las frecuencias de los cuatrigramas
    cuatrigramas_ingles = {
        "THAT": 0.761242,
        "THER": 0.604501,
        "WITH": 0.573866,
        "TION": 0.551919,
        "HERE": 0.374549,
        "OULD": 0.369920,
        "IGHT": 0.309440,
        "HAVE": 0.290544,
        "HICH": 0.284292,
        "WHIC": 0.283826,
        "THIS": 0.276333,
        "THIN": 0.270413,
        "THEY": 0.262421,
        "ATIO": 0.262386,
        "EVER": 0.260695,
        "FROM": 0.258580,
        "OUGH": 0.253447,
        "WERE": 0.231089,
        "HING": 0.229944
    }

    # Contar los cuatrigramas en el texto cifrado
    texto_cifrado_cuatrigrams = contar_ngramas(texto_cifrado, 4)

    # Calcular la frecuencia de los cuatrigramas en el texto cifrado
    texto_cifrado_cuatrigrams = dict(sorted(texto_cifrado_cuatrigrams.items()))
    texto_cifrado_cuatrigrams = {k: v / len(texto_cifrado) * 100 for k, v in texto_cifrado_cuatrigrams.items()}
    texto_cifrado_cuatrigrams = dict(sorted(texto_cifrado_cuatrigrams.items()))

    print()
    print('Frecuencias de los cuatrigramas en el texto cifrado y en el idioma inglés:')
    # Imprimir las frecuencias de los cuatrigramas en el texto cifrado y en el idioma inglés
    imprimir_frecuencias(texto_cifrado_cuatrigrams, cuatrigramas_ingles, 20)


def texto_desencriptado(texto_cifrado, llave):
    # Reemplazar las letras en el texto cifrado
    texto_cifrado_reemplazado = ''.join([llave[letra] if letra in llave else '.' for letra in texto_cifrado])
    # Imprimir como se ve el texto cifrado reemplazado
    return texto_cifrado_reemplazado


print("Bienvenido a tu programa de ayuda en la desencriptación de un texto cifrado.")
print("Por favor, ingresa el texto cifrado que deseas desencriptar:")
texto_cifrado = input()
contador_frecuencias(texto_cifrado)
print("Ingresa la llave que crees que se utilizó para encriptar el texto: (La entrada debe ser un diccionario, "
      "por ejemplo, {'A':'b', 'B':'c'})")
llave = input()
diccionario = ast.literal_eval(llave)
print("El texto desencriptado es:")
print(texto_desencriptado(texto_cifrado, diccionario))
while True:
    print("¿Deseas ingresar otra llave? (s/n)")
    respuesta = input()
    if respuesta == "n":
        break
    else:
        # Recordamos el texto cifrado y el contador de frecuencias
        print("Tu texto cifrado es:")
        print(texto_cifrado)
        contador_frecuencias(texto_cifrado)
        print("Ingresa la llave que crees que se utilizó para encriptar el texto:")
        llave = input()
        diccionario = ast.literal_eval(llave)
        print("El texto desencriptado es:")
        print(texto_desencriptado(texto_cifrado, diccionario))
print("Gracias por usar el programa.")

import string  # Libreria que permite usar el cod ASCII
from typing import List


def crear_tablero_vigenere(ESPAÑOL: bool) -> List[List[str]]:
    alfabeto = list(string.ascii_uppercase + ("Ñ" if ESPAÑOL else ''))
    # range retorna los valores de un array definida por el limite min y max
    tablero = [['' for _ in range(len(alfabeto))]
               for _ in range(len(alfabeto))]

    for i in range(len(alfabeto)):
        for j in range(len(alfabeto)):
            indice = (j + i) % len(alfabeto)
            tablero[i][j] = alfabeto[indice]

    return tablero


def vigenere(texto: str, clave: str, ESPAÑOL: bool, cifrar: bool) -> str:
    tablero = crear_tablero_vigenere(ESPAÑOL)
    resultado = ""
    # Define el tam de la clave tanto como el tam de texto
    clave_repetida = clave * (len(texto) // len(clave)) + \
        clave[:len(texto) % len(clave)]

    for i in range(len(texto)):
        if texto[i] in string.ascii_uppercase + ("Ñ" if ESPAÑOL else ""):
            if cifrar:  # Cifrado
                fila = string.ascii_uppercase.index(texto[i])
                columna = string.ascii_uppercase.index(clave_repetida[i])
                resultado += tablero[fila][columna]
            else:  # Descifrado
                fila = string.ascii_uppercase.index(clave_repetida[i])
                columna = tablero[fila].index(texto[i])
                resultado += string.ascii_uppercase[columna]
        else:
            resultado += texto[i]  # Si hay espacios en blanco

    return resultado

# Main


def main():
    ESPAÑOL = False  # Se define el tablero si es español -> true o ingles -> false
    texto_original = "YA ES PRIMAVERA EN EL CORTE INGLES"
    clave = "MARKETING"

    texto_cifrado = vigenere(
        texto_original.replace(" ", ""), clave, ESPAÑOL, True)
    print("Texto cifrado:", texto_cifrado)

    texto_descifrado = vigenere(texto_cifrado, clave, ESPAÑOL, False)
    print("Texto descifrado:", texto_descifrado)


if __name__ == "__main__":
    main()

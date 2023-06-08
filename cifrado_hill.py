from typing import List

ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


def generarMatrizClave(tam_matriz: int, clave: str) -> List[List[str]]:
    # Validamos el residuo
    if len(clave) % tam_matriz != 0:
        return "El tamaño de la matriz tiene que ser proporcional a la longitud de la clave"

    # Generamos la matriz
    matriz = [[0] * tam_matriz for _ in range(tam_matriz)]

    # Damos los valores a la matriz
    index = 0
    for i in range(tam_matriz):
        for j in range(tam_matriz):
            matriz[i][j] = clave[index]
            index += 1

    return matriz


def generarMatrizTexto(matriz_clave: List[List[str]], texto: str) -> List[List[str]]:
    tam_vector = len(matriz_clave[0])
    texto = texto.replace(" ", "")

    # Dividir el texto en segmentos de tamaño tam_vector
    segmentos = [texto[i:i+tam_vector]
                 for i in range(0, len(texto), tam_vector)]

    # Completar los segmentos con espacios en blanco
    segmento = [segmento.ljust(tam_vector, ' ')
                for segmento in segmentos]

    # Segmentar cada elemento de la matriz en vectores individuales
    matriz_aplanada = [elemento
                       for matriz in [[list(elemento[i:i+tam_vector])
                                       for i in range(0, len(elemento), tam_vector)]
                                      for elemento in segmento]
                       for elemento in matriz]

    return matriz_aplanada


def cifrado_hill(matriz_clave: List[List[str]], matriz_texto: List[List[str]]) -> str:

    C1 = (ALFABETO.index(matriz_clave[0][0]) *
          ALFABETO.index(matriz_texto[0][0])
          + ALFABETO.index(matriz_clave[0][1]) *
          ALFABETO.index(matriz_texto[0][1])
          + ALFABETO.index(matriz_clave[0][2]) *
          ALFABETO.index(matriz_texto[0][2])) % 27
    print(ALFABETO[C1])


def main():
    texto = "ESCRIBO LAS CANCIONES QUE HACEN CANTAR AL MUNDO ENTERO"
    a = "ESC RIB OLA SCA NCI ONE SQU EHA CEN CAN TAR ALM UND OEN TER O"
    tam_matriz = 3
    clave = "CANCIONES"

    matriz_clave = generarMatrizClave(tam_matriz, clave)
    # print(matriz_clave)

    matriz_texto = generarMatrizTexto(matriz_clave, texto)
    # print(matriz_texto)
    cifrado_hill(matriz_clave, matriz_texto)
    # print(ALFABETO['E'])


if __name__ == "__main__":
    main()

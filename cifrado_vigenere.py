ALFABETO = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'  # alfabeto español
LONGITUD_ALFABETO = len(ALFABETO)  # 27

# Crea un diccionario que mapea cada letra del alfabeto a su índice correspondiente [A: 0 ... Z: 26]
indice_letra = {letra: indice for indice, letra in enumerate(
    ALFABETO)}  # enumrate le da un indice a cada letra


def algoritmo_vigenere(texto: str, clave: str, cifrar: bool = True) -> str:
    texto = texto.upper()
    clave = clave.upper()
    resultado = ''
    k = 0  # índice inicial de la clave +concat -> texto
    operador = 1 if cifrar else -1
    for letra in texto:
        if letra in indice_letra:
            indice_texto = indice_letra[letra]
            indice_clave = indice_letra[clave[k]]
            indice_resultado = (indice_texto + (operador *
                                indice_clave)) % LONGITUD_ALFABETO
            resultado += ALFABETO[indice_resultado]
            k = (k + 1) % len(clave)
            # Se recorre clave hasta que se termine de recorrer texto, si clave ya fue recorrido en su totalidad, pero texto no, el % lo retorna a k = 0
        else:
            resultado += letra  # Si no lo encuentra en el alfabeto concatena en crudo
    return resultado


if __name__ == '__main__':
    mensaje = "UTPLAMEJORLURIGANCHO"
    clave = "LIMACENTER"
    mensaje_cifrado = algoritmo_vigenere(mensaje, clave, cifrar=True)
    mensaje_descifrado = algoritmo_vigenere(
        mensaje_cifrado, clave, cifrar=False)
    print(
        f'Texto Cifrado: {mensaje_cifrado}\nTexto Descifrado: {mensaje_descifrado}')

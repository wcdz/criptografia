DISTRIBUCION_BVORAK = "1234567890',.ÑPYFGCRL/=AOEUIDHTNS-;QJKXBMWVZ"


def mensaje_espacios(mensaje: str) -> str:
    return mensaje.replace(" ", "")


def clave_dinamica(clave: str, mensaje: str) -> str:
    return clave * (len(mensaje) // len(clave)) + \
        clave[:len(mensaje) % len(clave)]

def cantidad_bits_byte():
    return 0xFF.bit_length()

def cifrado(clave: str, mensaje: str) -> str:
    mensaje = mensaje_espacios(mensaje)
    clave = clave_dinamica(clave, mensaje)

    i = 0
    c = ""
    for m in mensaje:
        if (m in DISTRIBUCION_BVORAK):
            valor_letra_mensaje = DISTRIBUCION_BVORAK.index(m)
            # print(valor_letra_mensaje)
            valor_letra_clave = DISTRIBUCION_BVORAK.index(clave[i])
            # print(valor_letra_clave)
            calculo = ((valor_letra_mensaje -
                       valor_letra_clave) % len(DISTRIBUCION_BVORAK)) + cantidad_bits_byte()
            if calculo > len(DISTRIBUCION_BVORAK):
                calculo -= len(DISTRIBUCION_BVORAK)
            # print(calculo)
            operacion = DISTRIBUCION_BVORAK[calculo]
            c += operacion
            i += 1
    return c


def descifrado(clave: str, mensaje_cifrado: str) -> str:
    clave = clave_dinamica(clave, mensaje_cifrado)

    i = 0
    mensaje_descifrado = ""
    for c in mensaje_cifrado:
        if c in DISTRIBUCION_BVORAK:
            valor_letra_cifrado = DISTRIBUCION_BVORAK.index(c)
            valor_letra_clave = DISTRIBUCION_BVORAK.index(clave[i])
            calculo = ((valor_letra_cifrado - cantidad_bits_byte()) +
                       valor_letra_clave) % len(DISTRIBUCION_BVORAK)
            if calculo < 0:
                calculo += len(DISTRIBUCION_BVORAK)
            # print(calculo)
            operacion = DISTRIBUCION_BVORAK[calculo]
            mensaje_descifrado += operacion
            i += 1
    return mensaje_descifrado


def main():
    mensaje = "HOLA MUNDO"
    clave = "JA"
    cifrado_mensaje = cifrado(clave, mensaje)
    print("Mensaje cifrado:", cifrado_mensaje)
    descifrado_mensaje = descifrado(clave, cifrado_mensaje)
    print("Mensaje descifrado:", descifrado_mensaje)


if __name__ == '__main__':
    main()


# ALGORITMO
'''
1. UTILIZAR LA DISTRIBUCION DE BVORAK: 1234567890',.ÑPYFGCRL/=AOEUIDHTNS-;QJKXBMWVZ
2. LA CLAVE TIENE QUE SER DE LONGITUD DINAMICA, POR LO QUE VARIA DE ACUERDO AL MENSAJE
3. CALCULO PARA CIFRAR:
    ((valor_letra_mensaje - valor_letra_clave) mod longitud_bvorak) + cantidad_bits_byte
4. CALCULO DE DESCIFRADO:
    ((valor_letra_cifrado + valor_letra_clave) mod longitud_bvorak) - cantidad_bits_byte
5. El RECORRIDO EN EL ALFABETO ES DINAMICO POR LO QUE:
    CALCULO > longitud_bvorak:
        44 ... 0 
    CALCULO < 0:
        0 ... 44
'''
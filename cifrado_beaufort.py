'''ALFABETO = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', ' ']'''
ALFABETO = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789., '

def cifrado_beaufort(frase: str, clave: str) -> str:
    clave_repetida = clave * (len(frase) // len(clave)) + clave[:len(frase) % len(clave)]
    
    valores_f = []
    for caracter_f in frase.upper():
        valor_f = ALFABETO.index(caracter_f)
        valores_f.append(valor_f)
    # print(valores_f) 
    
    valores_c = []   
    for caracter_c in clave_repetida.upper():
        valor_c = ALFABETO.index(caracter_c)
        valores_c.append(valor_c)
    # print(valores_c)

    resta_mod = []
    for i in range(len(valores_f)):
        resta_mod.append((valores_f[i] - valores_c[i]) % len(ALFABETO))
    
    # print(resta_mod)
    resultado = []
    for valor in resta_mod:
        resultado.append(ALFABETO[valor])
    # print(resultado)

    return ''.join(resultado)
    
def descifrado_beaufort(cifrado: str, clave: str) -> str:
    clave_repetida = clave * (len(cifrado) // len(clave)) + clave[:len(cifrado) % len(clave)]

    valores_c = []
    for caracter_c in cifrado.upper():
        valor_c = ALFABETO.index(caracter_c)
        valores_c.append(valor_c)

    valores_cr = []
    for caracter_cr in clave_repetida.upper():
        valor_cr = ALFABETO.index(caracter_cr)
        valores_cr.append(valor_cr)

    suma_mod = []
    for i in range(len(valores_c)):
        suma_mod.append((valores_c[i] + valores_cr[i]) % len(ALFABETO))

    resultado = []
    for valor in suma_mod:
        resultado.append(ALFABETO[valor])

    return ''.join(resultado)

######################################################################
frase = "Mi celular es 978757642. Lamame, mas tarde. I love you"
clave = "Danyer"

cifrado_beaufort = cifrado_beaufort(frase, clave)
print(cifrado_beaufort)

descifrado_beaufort = descifrado_beaufort(cifrado_beaufort, clave)
print(descifrado_beaufort)

'''
@wcdz
@ajqs
'''
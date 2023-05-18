import random
alfabeto = {
    'A': ['27', '38', '41', '67', '77', '85', '99'],
    'B': ['10', '36', '59'],
    'C': ['05', '30', '44', '51', '81'],
    'D': ['11', '35', '68'],
    'E': ['20', '34', '43', '63', '76', '84', '92'],
    'F': ['06', '72'],
    'G': ['21', '49', '66'],
    'H': ['02', '37', '50', '82'],
    'I': ['25', '65', '75', '80', '94'],
    'J': ['12', '48', '58'],
    'K': ['08', '33'],
    'L': ['07', '13', '56', '69', '83'],
    'M': ['26', '42', '71'],
    'N': ['14', '29', '55', '64'],
    'Ñ': ['01', '57'],
    'O': ['22', '31', '74', '90'],
    'P': ['15', '46', '88'],
    'Q': ['19', '52'],
    'R': ['23', '47', '54', '79'],
    'S': ['04', '28', '45', '61'],
    'T': ['16', '53'],
    'U': ['32', '62', '78', '89', '92'],
    'V': ['18', '39', '73'],
    'W': ['09'],
    'X': ['03'],
    'Y': ['17', '40', '60'],
    'Z': ['24', '70'],
    ',': ['95'],
    '.': ['91'],
    ' ': ['93']
}

# Recorre nuestra entrada letra por letra
entrada = "COMO ESTAS"
cifrados = []
# CIFRADO
for e in entrada:
    valoresLetra = alfabeto[e]
    tamañoValoresL = len(valoresLetra)
    cifradoLetra = valoresLetra[random.randint(0, (tamañoValoresL-1))]
    # cifrados.append({e:cifradoLetra})
    cifrados.append(cifradoLetra)

print(cifrados)

# DESCIFRADO
descifrado = []
for v in cifrados:  # por cada letra se recorre el alfabeto
    for a in alfabeto:  # a es la letra
        if v in alfabeto[a]:
            descifrado.append(a)


print(descifrado)
print("".join(descifrado))

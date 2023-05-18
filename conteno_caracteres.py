# Funcion para transformar el texto y quitar caracteres especiales alfabeticos
def quitarCaracteres(c):
    caracteres = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u")
    )
    for a, b in caracteres:
        c = c.replace(a, b).replace(a.upper(), b.upper())
    return c

# Funcion para contarCaracteres


def contarCaracteres(texto):
    frecuencias = {}
    texto = quitarCaracteres(texto)
    for letra in texto:
        if letra.isalpha():  # [a-zA-Z]
            letra = letra.lower()  # minus
        if letra not in frecuencias:
            frecuencias[letra] = 1
        else:
            frecuencias[letra] += 1
    return dict(sorted(frecuencias.items())), len(texto.replace(" ", "").replace(",", "").replace(";", "").replace(".", "").replace(":", ""))


input = 'En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca que carnero, salpicón las más noches, duelos y quebrantos los sábados, lentejas los viernes, algún palomino de añadidura los domingos, consumían las tres partes de su hacienda. El resto de ella concluían sayo de velarte, calzas de velludo para las fiestas, con sus pantuflos de lo mismo, y los días de entre semana se honraba con su vellorí más fino. Tenía en su casa una ama que pasaba de los cuarenta, y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza, que así ensillaba el rocín como tomaba la podadera. Frisaba la edad de nuestro hidalgo con los cincuenta años; era de complexión recia, seco de carnes, enjuto de rostro, gran madrugador y amigo de la caza. Quieren decir que tenía el sobrenombre de Quijada, o Quesada'

print(contarCaracteres(input))

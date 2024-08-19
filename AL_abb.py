import re

# Expresión regular para cadenas que terminen en "abb"
pattern = r'.*abb$'

# Función para verificar si una cadena cumple con la expresión regular
def check_string(s):
    return re.fullmatch(pattern, s) is not None

# Lista de cadenas para probar
test_strings = [
    "abb",
    "aabb",
    "babb",
    "aaabb",
    "ababb",
    "baabb",
    "bbabb",
    "randomstring",
    "abbxyz",
]

# Probar las cadenas y mostrar los resultados
for string in test_strings:
    if check_string(string):
        print(f'"{string}" cumple con la expresión regular.')
    else:
        print(f'"{string}" NO cumple con la expresión regular.')

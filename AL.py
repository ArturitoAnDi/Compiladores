import re

# Definir patrones para los tokens
token_patterns = {
    'KEYWORD': r'\b(?:if|else|while|for|return)\b',  # Palabras clave
    'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',  # Identificadores
    'NUMBER': r'\b\d+\b',  # Números
    'WHITESPACE': r'\s+',  # Espacios en blanco
    'COMMENT': r'//.*',  # Comentarios de una línea
    'UNKNOWN': r'.'  # Cualquier otro carácter
}

def tokenize(code):
    # Crear una lista de expresiones regulares ordenadas por longitud (de mayor a menor)
    sorted_patterns = sorted(token_patterns.items(), key=lambda pair: -len(pair[1]))
    
    tokens = []
    while code:
        match = None
        for token_name, pattern in sorted_patterns:
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                if token_name != 'WHITESPACE' and token_name != 'COMMENT':  # Ignorar espacios y comentarios
                    tokens.append((token_name, match.group(0)))
                code = code[match.end():]  # Avanzar en el código
                break
        if not match:
            raise ValueError(f"Unexpected character sequence: {code}")
    
    return tokens

# Ejemplo de código fuente
source_code = '''
if x > 10 {
    y = 20;
    // Esto es un comentario
    return y;
}
'''

# Tokenizar el código fuente
tokens = tokenize(source_code)

# Imprimir los tokens
for token in tokens:
    print(token)

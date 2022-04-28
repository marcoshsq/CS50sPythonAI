"""A função print recebe algum objeto e 
imprime ele na tela ou no console.
"""

# Exemplo 01:

print("Oi, eu sou o computador!")
# Saída: Oi, eu sou o computador!

# Exemplo 02:


# A função print receber alguns parâmetros

print("Hello, World!")  # Saída: Hello, World!

print(
    "Hello", "World!", sep=","
)  # esse (sep="") separa as partes da string com o simbolo passado dentro das aspas

print("Hello", "World", sep="**")  # Saída: Hello**World
print("Hello", "World", sep="//")  # Saída: Hello//World

print(
    "Hello", end="*-*-*"
)  # o end coloca o conteúdo dentro das aspas no final da string
# Saída: Hello*-*-*

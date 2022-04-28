"""

Python é completamente orientado a objetos e não "digitado estaticamente".
Não é necessário declarar variáveis antes de usá-las, graças a deus por isso,
ou declarar seu tipo. Cada variável em Python é um objeto.

Ao contrário de outras linguagens de programação, Python não tem comando para
declarando uma variável. Uma variável é criada no momento em que você atribui pela primeira vez
um valor para isso.

Uma variável pode ter um nome curto (como x e y) ou um nome mais descritivo
(idade, carname, total_volume).

Regras para variáveis Python:

- Um nome de variável deve começar com uma letra ou o caractere sublinhado.

- Um nome de variável não pode começar com um número.

- Um nome de variável pode conter apenas caracteres alfanuméricos e sublinhados (A-z, 0-9 e _ ).

- Os nomes das variáveis diferenciam maiúsculas de minúsculas 
(idade, idade e IDADE são três variáveis diferentes).

"""

# Já em relação à estilo: “Explícito é melhor que implícito.” - The Zen of Python.

# Para nomear variáveis tem duas diretrizes :
# 1. Use uma única letra minúscula, palavra ou palavras. Separe as
# palavras com sublinhados para melhorar a legibilidade. Exemplo:

x = 1
y = 2
z = x + y

# 2. Use nomes simples, descritivos e memoráveis:

num_01 = 1
num_02 = 2
soma_num = num_01 + num_02

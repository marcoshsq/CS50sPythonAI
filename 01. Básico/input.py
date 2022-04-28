"""A função de entrada (input) permite receber dados do usuário. 
Por padrão, os dados são do tipo string (texto), mas é possível 
alterá-los fazendo conversão de tipo (type casting)."""

# Exemplo:
name = input("Qual o seu nome? ")
print(f"Olá {name}, prazer em te conhecer!")
print("Olá {}, prazer em te conhecer".format(name))
print(
    "Olá", name + ", prazer em te conhecer!"
)  

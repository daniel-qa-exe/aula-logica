nome = "PAULA MARTINS"
mes = "JANEIRO"
valor = 500,00
desconto = "10%"
cupom = "PAULAÉ10"

#tipos de format 
format_1 = f"O nome da pessoa é {nome}, desconto dela é {desconto}"
format_2 = "o nome da pessoa é {}, desconto dela é {}".format(nome,desconto)
format_3 = "o nome da pessoa é {a}, desconto dela é {b}".format(a = nome, b = desconto)

print(format_1)
print(format_2)
print(format_3)

#função de tipagem de dados 
tipo_var = type(nome)
print(tipo_var)
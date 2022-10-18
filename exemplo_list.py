frutas = ["Maçã", "Uva", "Banana", "Manga", "Laranja", "Limão"]
print(frutas)
print(type(frutas))
print("Conteúdo do índice 1: ", frutas[1])
print("Total de frutas armazenadas: ", len(frutas))
print("Temos Manga? ", "Manga" in frutas)
print("Temos Morango? ", "Morango" in frutas)
# Fim do slide 5

frutas.append("Morango") #Adiciona ao final
print("\n", frutas)
print("Temos Morango? ", "Morango" in frutas)
print("Índice para Laranja em frutas: ", frutas.index("Laranja"))

frutas.remove("Uva") #Remove o item apontado
print("\n", frutas)
print("Índice para Laranja em frutas: ", frutas.index("Laranja"))

del frutas[4] #Remove item pelo índice apontado
print("\nQuem foi removido?" )
print(frutas)
# Fim do slide 6

frutas.insert(2, "Abacaxi") #Adiciona item na posição apontada (cria a posição),
print("\n", frutas)
print("Índice para Laranja em frutas: ", frutas.index("Laranja"))
print("Qual o índice do Abacaxi? ", frutas.index("Abacaxi"))

print("\n", frutas)
frutas[3] = "Acerola" #Altera o valor na posição apontada
print(frutas)

print("\n", frutas)
print(f"Total de itens no list: { len(frutas) }") #total de itens
# Fim do slide 7

ft = input("\nDigite uma fruta: ")
if (ft in frutas):
    print(f"{ft} existe no list frutas")
else:
    print(f"{ft} não existe no list frutas")

print("\n", frutas)
print("Quantidade do item \"Laranja\" no list frutas: ", frutas.count("Laranja") ) #Contagem de itens
print("Quantidade do item \"Uva\" no list frutas: ", frutas.count("Uva") )
# Fim do slide 8

#Reverse
print("\n", frutas)
frutas.reverse()
print(frutas)

#Sort (Ordem Ascendente)
print("\n", frutas)
frutas.sort()
print(frutas)
# Fim do slide 9
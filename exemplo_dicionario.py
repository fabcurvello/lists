"""
Dicionários são como as listas dinâmicas, só que não são indexados a partir do zero, e sim,
por chaves, definidas durante o cadastro dos valores.
"""
#Listas dinâmicas utilizam colchetes []"
#Tuplas utilizam parênteses ()"
#Dicionários utilizam chaves {}

verbos = {
    "pular": "elevar-se do chão por impulso dos pés e das pernas",
    "cair": "ir ao chão",
    "devolver": "entregar ou enviar de volta"
}

print(verbos)
print(type(verbos))

print(verbos["cair"]) #ir ao chão


carro = {
    "fabricante": "VW",
    "modelo": "Fusca",
    "cor": "Verde",
    "ano": 1975,
    "donos": ["João", "José", "Maria"]
}
#OBS: Dentro do dicionário carro, donos possui conteúdo de lista dinâmica,
print(carro)
print(carro["modelo"]) # Fusca
# Fim do slide 18

print(carro["donos"])
carro["donos"].append("Maria") # Adiciona um item ao LIST donos. Não existe append em dicionários
print(carro["donos"])
print(carro["donos"][1]) # José

carro['km'] = 115000 # Adiciona uma chave/valor ao final do dicionário
print(carro)

carro['km'] = 173000 # Modifica o valor de uma chave já existente
print(carro)
# Fim do slide 19

carro.update({"cor": "Amarelo"}) # Outra forma de modificar o valor de uma chave já existente. Também funciona para adicionar chave/valor quando a chave não existe
print(carro)

del carro["km"] # Remove a chave km e o seu valor correspondente
print(carro)

removido = carro.pop("cor") # Remove a chave e o valor correspondente, porém, salva o valor na var removido
print(carro)
print(removido)
#Fim do slide 20

print(carro.keys()) # Somente as chaves
print(carro.values()) # Somente os valores

print(carro.items()) # Separa chave/valor em tuplas dentro de uma lista

print(carro.get("fabricante")) # VW
print(carro.get("cor", "Azul")) # Exibe o valor da chave. Se a chave não existir, ele exibe o valor padrão (nesse caso, azul)

print(len(carro)) # 4 -> Total de itens chave/valor (fabricante, modelo, ano, donos)

carro.clear() # limpa todos os itens do dicionário carro
print(carro) # {}
#Fim do slide 21

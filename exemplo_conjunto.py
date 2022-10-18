"""
Conjuntos (sets), são listas NÃO INDEXADAS
também são declarados utilizando chaves { } como os dicionários,
mas não possuem a chave de indexação para cada item. Somente o valor de cada item.
"""

nomes = { "João", "Maria", "Pedro", "José", "Ana" }
print(type(nomes)) # set
print(nomes)

nomes.add("Jorge")
print(nomes)

nomes.remove("Jorge")
print(nomes)

nomes.add("Maria") # Não consegue adicionar item repetido
print(nomes)
# Fim do slide 24

nomes2 = { "Vanessa", "Jéssica", "Maria", "Ana", "Simone" }
print(nomes2)

uniao = nomes.union(nomes2) # União dos 2 conjuntos (sem repetições)
print(uniao)

itersecao = nomes.intersection(nomes2) # Interseção (somente os comuns aos 2 conjuntos)
print(itersecao)
# Fim do slide 25
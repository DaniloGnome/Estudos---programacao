#mostrar o tipo da classe, no caso TUPLE
tp_frutas = ('maça','laranja','goiaba')
print(type(tp_frutas))

#mostrar o segundo semestre do ano dentro de uma tuple
tp_meses = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
print(tp_meses[3:6])

#ordenar uma tuple, pelo DDD
uf_cod = [('PE',81),('RJ',21),('SP',11),('PB',83)]
print(sorted(uf_cod, key = lambda x:x[1]))

#desempacotamento de valores
def nome_idade_uf():
    nome = "Jose"
    idade = 28
    uf = 'RN'
    return nome,idade,uf
name,age,state = nome_idade_uf()
print(name,age,state)

#mapeamento de valores
alunos = ('Kelly','Adauto','Marcelino','Luana','Henrique')
notas = (5.5,8,9,6.5,7)

av1 = tuple(zip(alunos,notas)) # o tuple será o tipo da variavel e o zip para unir as duas tuples(alunos,notas)
print(av1)

#1 Escreva uma função que receba duas tuplas como entrada
# e retorne uma única tupla que seja a concatenação das duas
def funcao_tuple (nome_carro,valor_carro):
    return nome_carro+valor_carro
nome_carro = ('Uno','Corsa','Onix')
valor_carro = (23.000,40.000,70.000)
total = tuple(zip(nome_carro, valor_carro))
print(total)

#2 Escreva uma função que receba uma tupla contendo o
# nome e endereço contendo, logradouro, número e bairro de uma pessoa e retorne uma string formatada.
def funcao_registro(tupla):
    nome,logradouro,numero,bairro = tupla
    return f'nome :{nome},residente :{logradouro},{numero},{bairro}'
dados = ('danilo','rua da alegria','275','ipes')
print(funcao_registro(dados))

#3 Escreva uma função que receba uma lista de
# tuplas contendo nome e idade de pessoas e
# retorne a lista ordenada por idade.



lista_nomes = ('Danilo','Daniel','Mardony','Bruno')
idade_grupo = (29,20,20,19)

def receba_lista(lista_nomes,idade_grupo):
    listacompleta = tuple(zip(lista_nomes, idade_grupo))
    return
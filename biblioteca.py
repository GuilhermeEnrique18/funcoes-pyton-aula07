from functools import total_ordering


def imprimeNome(nome):
    print(f"Nome: {nome}")

def solicitarNome():
    nome = input("Digite seu nome: ")
    return nome

def contaVogais(texto):
    cont = 0
    for i in range(0, len(texto)):
        if texto[i] == "a" or texto[i] == "e" or texto[i] == "i" or texto[i] == "o" or texto[i] == "u":
            cont += 1
    print(cont)

def estoque (produto,qtd,valorUnitario):
    valorTotal = qtd * valorUnitario
    return valorTotal

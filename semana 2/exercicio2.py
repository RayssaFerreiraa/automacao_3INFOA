'''
Exercício 2:
Crie um programa que lê do teclado a nota
e a quantidade de faltas de um aluno. O
programa deve imprimir reprovado, se:
A nota for menor que 6 ou se as presencas
forem menor do que 75 e aprovado 
caso contrário.
'''
nota = int(input("Digite sua nota: "))
faltas = int(input("Digite sua quantidade de faltas: "))

if nota < 6:
    print(nota, "Reprovado!")
else :
    print(nota, "Aprovado!")

if faltas > 75:
    print(faltas,"Reprovado!")
else:
    print(faltas,"Aprovado!")


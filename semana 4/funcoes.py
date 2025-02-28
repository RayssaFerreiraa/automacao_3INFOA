'''
As funções permite modularizar o código, dividir ele em partes 
menores que podem ser reaproveitadas. Isso simplifica a codificação.

Estrutura função em python

def nome_funcao(param1,param2,paramN):
 //algum codigo que a função faz return saida_da_funcao

'''
#cria uma função que calcula a área do triângulo
def CalculateTrianglArea(base, altura):
   area = (base * altura) /2
   return area

#cria uma função que calcula a área do triângulo
def CalculateSquareArea(lado):
   area = lado * lado
   return area

'''
#Exemplo 1: Chamar a função
area1 = CalculateTrianglArea(100, 10)
print ("A área do triângulo 1 é", area1)

#Exemplo 2: Chamar a função novamente
base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))
area2 = CalculateTrianglArea(100, 10)
print ("A área do triângulo 2 é", area2)
'''
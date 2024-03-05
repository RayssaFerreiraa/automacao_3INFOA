'''
Exercício 3 - Semana 3
Crie um programa que lê do teclado
sucessivos números de matricula (int).
O programa deve parar de ler os números 
quando a matricula 0 for digitada.
Ao final deve apresentar os números de 
matriculas separados em 3 grupos.
'''
matriculas=[]
grupo1=[]
grupo2=[]
grupo=[]

while True:
    matricula = int(input("Digite a matrícula (Digite 0 até parar):"))
    if matricula == 0:
        break 
    matriculas.append(matricula)

    for i, matricula in enumerate(matriculas):
        if i % 3 == 0:
            grupo1.append(matricula)
            
        else:
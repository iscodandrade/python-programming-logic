"""
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular 
a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

nota1 = float(input('Insira a primeira nota ----> '))
nota2 = float(input('Insira a segunda nota -----> '))
nota3 = float(input('Insira a terceira nota ----> '))

media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print('Média ---> 10\nO aluno foi aprovado com distinção.')
elif media >= 7:
    print('Média --->', media, '\nO aluno foi aprovado.')
elif media < 7:
    print('Média --->', media, '\nO aluno foi reprovado.')

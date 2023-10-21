#Lista 3 - Exercício 5

a = int(input('Informe um número inteiro: '))
b = int(input('Informe um número inteiro: '))
c = int(input('Informe um número inteiro: '))
if a > b and a > c:
    print(f'{a} é o maior valor informado.')
elif b > a and b > c:
    print(f'{b} é o maior valor informado.')
elif c > a and c > b:
    print(f'{c} é o maior valor informado.')
elif a == b or a == c:
    print(f'{a} é o maior valor informado.')
else:
    print(f'{b} é o maior valor informado.')

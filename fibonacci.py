# Testando a função
num = int(input("Digite um número: "))

def is_fibonacci(n):
    if n < 0:
        return False
    # Os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

#Criamos uma função
def fibonacci(i):
    if i==0:
        return  0
    elif i==1:
        return 1
    else:
        return fibonacci(i-2) + fibonacci(i-1)

 #Aqui temos um laço de repetição que vai printar
 #a sequência de Fibonacci
for x in range(20):
    print(fibonacci((x)))


if is_fibonacci(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")

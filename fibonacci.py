


def fibonacci(n):
    sum = 0
    if n == 0:
        return sum
    sum = 1
    anterior = 1
    print(sum)
    for i in range(1, n):
        temp = sum
        sum = sum + anterior
        print(sum)
        anterior = temp
        

fibonacci(9)
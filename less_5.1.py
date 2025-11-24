import random
a = random.randit(0,100)
b = random.randit(0,100)
c = random.randit(0,100)
array1 = [random.randint(0, 100) for i in range(a)]
array2 = [random.randint(0, 100) for i in range(b)]
array3 = [random.randint(0, 100) for i in range(c)]
maxit = max(max(array1), max(array2), max(array3))
summa = sum(array1) + sum(array2) + sum(array3)
print("Массив 1:", array1)
print("Массив 2:", array2)
print("Массив 3:", array3)
print(maxit)
print(summa)



























































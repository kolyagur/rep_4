#факториал f_n
f_n=5

def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n
  
print(f'Факториал числа {f_n} =',factorial(f_n))
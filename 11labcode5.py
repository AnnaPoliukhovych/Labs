#Обчислення інтегралу методом трапецій
from scipy import integrate 
import numpy as np

# Задаємо функцію, яку необхідно інтегрувати
def f(x):
    return 1 / np.sqrt(1 + 2 * x**2)

# Задаємо межі інтегрування та початкову кількість розбиттів
a = 0.6
b = 1.5
n = 20

# Обчислюємо значення інтегралу методом трапецій
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = a
    sum = 0
    for i in range(1, n):
        x += h
        sum += 2 * f(x)
    sum += f(b)
    integral = h / 2 * sum

    return integral

# Обчислюємо значення інтегралу методом трапецій з точністю 0.001
#Перевірка точності за правилом Рунге
integral1 = trapezoidal_rule(f, a, b, n)
n *= 2
integral2 = trapezoidal_rule(f, a, b, n)
while abs(integral2 - integral1) / 3 > 0.001:
    integral1 = integral2
    n *= 2
    integral2 = trapezoidal_rule(f, a, b, n)

# Виводимо результат
print("Trapetzia methodof:", round(integral2, 3))

v,err = integrate.quad(f,3.2,4) #Перевірка
print("Check for the trapetzia method= ",round(v, 5))

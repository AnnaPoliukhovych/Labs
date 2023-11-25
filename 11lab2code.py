#Обчислення інтеграла методом Симпсона
from scipy import integrate 
import numpy as np

# Задаємо функцію, яку необхідно інтегрувати
def f(x):
    return 1 / np.sqrt(12 * x + 0.5)

# Задаємо межі інтегрування та початкову кількість розбиттів
a = 0.6
b = 1.4
n = 10

# Обчислюємо значення інтегралу методом Симпсона
def simpson_rule(f, a, b, n):
    h = (b - a) / n 
    integr = f(a) + f(b) 
    for i in range(1,n): 
        k = a + i*h 
        if i%2 == 0: 
            integr += 2 * f(k) 
        else: 
            integr += 4 * f(k) 
    integr *= h/3 
    return integr 

# Обчислюємо значення інтегралу методом Сімпсона з точністю 0.001
integral1 = simpson_rule(f, a, b, n)
n *= 2
integral2 = simpson_rule(f, a, b, n)
while abs(integral2 - integral1) / 15 > 0.001:
    integral1 = integral2
    n *= 2
    integral2 = simpson_rule(f, a, b, n)
# Виводимо результат
print("Simpsone method:", round(integral2, 3))

v,err = integrate.quad(f,a,b)#Перевірка 
print("Check for the simpsone method= ",round(v, 3))

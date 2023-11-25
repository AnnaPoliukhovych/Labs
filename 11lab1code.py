#Обчислення інтеграла методом прямокутників
from scipy import integrate 
import numpy as np
eps = 0.001
a = 0.6
b = 1.4
n = 10
def f1(x): 
    return 1 / np.sqrt(12 * x + 0.5)
def left_rec(f1,a,b,n): 
    h=(b-a)/n 
    sum=0 
    for i in range(0,n): 
        sum+=f1(a+i*h) 
    return sum*h 

v,err = integrate.quad(f1,a,b)#Перевірка
#Перевірка точності за правилом Рунге:
if abs(left_rec(f1,a,b,2*10) - left_rec(f1,a,b,10))/3. <=eps:
    print("left rectangle:",round (left_rec(f1,a,b,10), 5)) 
def right_rec(f1,a,b,n): 
    h=(b-a)/n 
    sum=0 
    for i in range(1,n+1): 
        sum+=f1(a+i*h) 
    return sum*h 
print("right rectangle:",round (right_rec(f1,a,b,10), 5)) 
def aver_rec(f1,a,b,n): 
    h=0.08 
    sum=0 
    for i in range(0,n): 
        sum+=f1(a+i*h) 
    return sum*h 
print("average rectangle:",round (aver_rec(f1,a,b,10), 5)) 
print("Check for the rectangle method= ",round (v, 5))
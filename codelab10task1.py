import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Задана функція
def my_function(x):
    return 2 * np.sin(x) + 2 * x

# Значення x з таблиці
x_values = np.array([0.1 * i for i in range(10)])

# Відповідні значення y
y_values = my_function(x_values)

# Створення DataFrame з даними
data = {'i': range(10), 'xi': x_values, 'f(xi)': y_values}
df = pd.DataFrame(data)

# Побудова графічної таблиці
fig, ax = plt.subplots()
ax.axis('off')  # Вимкнемо вісі для графічної таблиці
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc = 'center', loc='center', colColours=['#f3f3f3']*df.shape[1])

# Налаштування стилю графічної таблиці
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)  # Збільшимо розмір таблиці

plt.show()
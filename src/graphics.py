import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()
 
x = [f'H{i+1}' for i in range(10)]
y = np.random.randint(1, 5, len(x))
ax.bar(x, y)
 
plt.show()
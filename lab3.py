import matplotlib.pyplot as plt
import numpy as np

data_file = 'DS4.txt'
data = np.loadtxt(data_file)

alpha = 10 * (4 + 1)
alpha = np.deg2rad(alpha)  
rotation_matrix = np.array([[np.cos(alpha), -np.sin(alpha)],
                            [np.sin(alpha), np.cos(alpha)]])

transformed_data = np.dot(data - [480, 480], rotation_matrix) + [480, 480]

fig, ax = plt.subplots(figsize=(960/80, 960/80), dpi=80)

ax.scatter(transformed_data[:, 0], transformed_data[:, 1], s=10, c='b', marker='o', label='Точки після перетворення')

ax.set_xlabel('Вісь X')
ax.set_ylabel('Вісь Y')
ax.set_title('Графік точок після афінного перетворення')

ax.legend()

output_file = 'output_graph.png'
plt.savefig(output_file)

plt.show()
print(f"Графік після афінного перетворення збережено у файлі: {output_file}")

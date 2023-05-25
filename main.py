import numpy as np
import matplotlib.pyplot as plt

f = np.array([3, 5, 7])
np.concatenate((f, f))

f = np.array([[3], [5], [7]])
np.concatenate((f, f))

np.concatenate((f, f), axis=1)

x = np.array([3, 5, 7])
r = np.array([8, 15, 23])

fig, ax = plt.subplots()
ax.plot(x, r, "bo")
fig.show()

X = np.concatenate((np.power(x.reshape(x.shape[0], 1), 0),
                    np.power(x.reshape(x.shape[0], 1), 1),
                    np.power(x.reshape(x.shape[0], 1), 2),
                   ),
                   axis=1)
w = np.linalg.inv(X) @ r.reshape(r.shape[0], 1)
print(w)

xs = np.arange(0, 7.1, 0.01)
Xs = np.ones((xs.shape[0], 1))
for i in range(1, X.shape[0]):
    Xs = np.concatenate((Xs,
                         np.power(xs.reshape(xs.shape[0], 1), i)),
                        axis=1)

fig, ax = plt.subplots()
y = Xs @ w
ax.plot(x, r, "bo", label="Datos")
ax.plot(xs.reshape(xs.shape[0], 1), y, "g-", label="Curva")
ax.legend()
fig.show()

input("Presiona Enter para salir.")
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set(xlim=(-10,10),ylim=(-10,10))
ax_circle = plt.Circle((0,0),(5,5))
fig.add_artist(ax_circle)
plt.plot(fig)
plt.show()
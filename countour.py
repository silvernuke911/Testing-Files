import matplotlib.pyplot as plt
import numpy as np

delta = 0.025

x = y = np.arange(-3.0, 3.01, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

nr, nc = Z.shape

# put NaNs in one corner:
Z[-nr // 6:, -nc // 6:] = np.nan
# contourf will convert these to masked


Z = np.ma.array(Z)
# mask another corner:
Z[:nr // 6, :nc // 6] = np.ma.masked

# mask a circle in the middle:
interior = np.sqrt(X**2 + Y**2) < 0.5
Z[interior] = np.ma.masked

fig1, ax2 = plt.subplots(layout='constrained')
CS = ax2.contourf(X, Y, Z, 10, cmap=plt.cm.bone)

# Note that in the following, we explicitly pass in a subset of the contour
# levels used for the filled contours.  Alternatively, we could pass in
# additional levels to provide extra resolution, or leave out the *levels*
# keyword argument to use all of the original levels.

# CS2 = ax2.contour(CS, levels=CS.levels[::2], colors='r')

ax2.set_title('Nonsense (3 masked regions)')
ax2.set_xlabel('word length anomaly')
ax2.set_ylabel('sentence length anomaly')

# Make a colorbar for the ContourSet returned by the contourf call.
cbar = fig1.colorbar(CS)
cbar.ax.set_ylabel('verbosity coefficient')
# Add the contour line levels to the colorbar
# cbar.add_lines(CS2)

plt.show()

x=y=np.arange(-5,5,0.01)
x,y=np.meshgrid(x,y)

def func(x,y,t=1):
    return np.cos(x)*np.sin(y)*np.sin(t)

z=func(x,y)

fig=plt.figure(figsize=(6,6))
levels = np.linspace(-1, 1, 101)
ax=fig.add_subplot()
contour=ax.contourf(x,y,z,cmap='inferno',levels=levels,vmin=-1,vmax=1)
fig.colorbar(contour,ax=ax,shrink=0.75,aspect=15,label='luminosity',ticks=np.linspace(-1,1,10+1),extend="max",location="right")
# contour=ax2.contourf(x,y,z,cmap='inferno',levels=levels,vmin=0,vmax=1)
ax.set_title('Contour Plot',fontname = 'times new roman')
ax.set_aspect(1)
ax.set_xlabel('x-axis (cm)')
ax.set_ylabel('y-axis (cm)')
plt.show()




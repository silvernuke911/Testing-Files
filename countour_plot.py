import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
# matplotlib.pyplot.title(r'ABC123 vs $\mathrm{ABC123}^{123}$')

x=np.linspace(-5, stop=5,num=1000)
y=np.linspace(-5, stop=5,num=1000)
x,y=np.meshgrid(x,y)

def norm_dist(x,sigma=1,mean=0):
    coeff=1/(sigma*np.sqrt(2*np.pi))
    expo=-0.5*((x-mean)/sigma)**2
    return coeff*np.exp(expo)

def double_slit_experiment(x,slit_distance=0.025,slit_width=0.025,wavelength=0.0000650,screen_distance=90):
    theta=np.arctan(x/screen_distance)
    def sinc(x):
        return np.sin(x)/x
    def sinc_term(x):
        return sinc(np.pi*slit_width*np.sin(x)/wavelength)
    def cos_term(x):
        return np.cos(np.pi*slit_distance*np.sin(x)/wavelength)
    return (cos_term(theta)**2)*(sinc_term(theta)**2)

def z_func(x,y):
    return np.exp(-(x**2+y**2))
# np.sin(x)*np.cos(y)
# np.exp(-(x**2+y**2))
# double_slit_experiment(x)*norm_dist(y,sigma=0.0125)

z=z_func(x,y)

fig=plt.figure(figsize=(14,6))
ax = fig.add_subplot(121,projection='3d')
ax.plot_surface(x,y,z,cmap='hot')
ax.set_title('3D Plot')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')

# Defining contour levels
levels = np.linspace(0, 1, 101)

ax2=fig.add_subplot(122)
#contour=ax2.contour(x,y,z,cmap='viridis')
contour=ax2.contourf(x,y,z,cmap='inferno',levels=levels,vmin=0,vmax=1)
fig.colorbar(contour,ax=ax2,shrink=0.75,aspect=15,label='luminosity',ticks=np.linspace(-1,1,10+1),extend="max",location="right")
# ax2.set_ylim(-0.2,0.2)
# ax2.set_xlim(-1,1)
# ax2.set_ylim(-5,5)
# ax2.set_xlim(-5,5)
ax2.set_aspect(1)
ax2.set_title('Contour Plot',fontname = 'times new roman')
ax2.set_xlabel('x-axis (cm)')
ax2.set_ylabel('y-axis (cm)')
plt.tight_layout()
plt.show()

#inferno, viridis, hot, afmhot, plasma,jet,magma
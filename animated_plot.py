import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
#from matplotlib.animation import FFMpegWriter
#plt.rcParams['animation.ffmpeg_path'] = 'C:\\Users\\spsha\\Desktop\\ffmpeg-4.4-full_build\\bin\\ffmpeg.exe'
# This is the final example I showed in the code - notice I have 2 "cursor marks" not shown in the video
fig = plt.figure()
l, = plt.plot([], [], 'k-')
# l2, = plt.plot([], [], 'm--')
# p1, = plt.plot([], [], 'ko')
# p2, = plt.plot([], [], 'mo')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('title')

plt.xlim(-5, 5)
plt.ylim(-2, 2)

def func(x):
    return np.sin(x)

xlist=np.linspace(-5,5,100)
ylist=func(xlist)
# l.set_data(xlist,ylist)
# plt.show()

metadata = dict(title='Movie', artist='silver')
writer = PillowWriter(fps=15, metadata=metadata)
# writer = FFMpegWriter(fps=15, metadata=metadata)

xlist=[]
ylist=[]

with writer.saving(fig, "sinWave2.gif", 100):
    for xval in np.linspace(-5,5,100):
        xlist.append(xval)
        ylist.append(func(xval))
        l.set_data(xlist,ylist)
        writer.grab_frame()
        plt.pause(0.001)
        plt.clf()
plt.close()
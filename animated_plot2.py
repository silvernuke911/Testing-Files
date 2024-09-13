import numpy as np
import matplotlib
# matplotlib.use("Agg") # useful for a webserver case where you don't want to ever visualize the result live.
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter, PillowWriter
import time

# Change to reflect your file location!
# plt.rcParams['animation.ffmpeg_path'] = 'C:\\Users\\spsha\\Desktop\\ffmpeg-4.4-full_build\\bin\\ffmpeg.exe'


# Fixing random state for reproducibility
np.random.seed(19680801)

frame_fps=20

metadata = dict(title='Movie', artist='silver')
writer = PillowWriter(fps=frame_fps, metadata=metadata)
#writer = FFMpegWriter(fps=15, metadata=metadata)

def progress_bar(progress, total, start_time, scale=0.50):
    # Creates a progress bar on the command line, input is progress, total, and a present start time
    # progress and total can be any number, and this can be placed in a for or with loop

    percent = 100 * (float(progress) / float(total))                        # Calculate the percentage of progress
    bar = '█' * round(percent*scale) + '-' * round((100-percent)*scale)     # Create the progress bar string
    elapsed_time = time.time() - start_time                                 # Calculate elapsed time
    if progress > 0:                                                        # Estimate total time and remaining time
        estimated_total_time = elapsed_time * total / progress
        remaining_time = estimated_total_time - elapsed_time
        remaining_seconds = int(remaining_time)
        remaining_milliseconds = int((remaining_time - remaining_seconds) * 1_000)
        remaining_str = time.strftime("%H:%M:%S", time.gmtime(remaining_seconds))
        remaining_str = f"{remaining_str}.{remaining_milliseconds:03d}"
    else:
        remaining_str = '...'
    print(f'|{bar}| {percent:.2f}% Time remaining: {remaining_str}  ', end='\r')    # Print the progress bar with the remaining time
    if progress == total: 
        elapsed_seconds = int(elapsed_time)
        elapsed_ms=int((elapsed_time-elapsed_seconds)*1000)                         # Print elapsed time when complete
        elapsed_seconds =  time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        print('\n'+f'Elapsed time : {elapsed_seconds}.{elapsed_ms:03d}')


x=y=np.arange(-5,5,0.01)
x,y=np.meshgrid(x,y)



def anim_3d_contour():

    def func(x,y,t=1):
        return np.cos(x)*np.sin(y)*np.sin(t)

    z_min,z_max=-1,1
    z=func(x,y)
    fig=plt.figure(figsize=(8,6))
    levels = np.linspace(z_min, z_max, 101)
    ax=fig.add_subplot()

    contour=ax.contourf(x,y,z,cmap='inferno',levels=levels,vmin=z_min,vmax=z_max)
    fig.colorbar(contour,ax=ax,shrink=0.75,aspect=15,label='luminosity',ticks=np.linspace(z_min,z_max,10+1),extend="max",location="right")

    print('Starting Render')
    start_time = time.time()
    with writer.saving(fig, "exp3d4.gif", 100):
        for t in np.linspace(0,20,21):
            z=func(x,y,t)
            contour=ax.contourf(x,y,z,cmap='inferno',levels=levels,vmin=z_min,vmax=z_max)
            ax.set_aspect(1)
            writer.grab_frame()
            plt.cla()
            progress_bar(t,20,start_time)
    print('Render')


def anim_3d_contour2():

    time_play=1
    nframes=round(time_play*frame_fps)+1

    def func(x,y,t):
        c=2
        return np.exp(-t)*np.exp(-((time_play-t)**2)*((c-np.sqrt(x**2+y**2))**2))

    z_min,z_max=0,1
    z=func(x,y,1)
    fig=plt.figure(figsize=(8,6))
    levels = np.linspace(z_min, z_max, 101)
    ax=fig.add_subplot()

    contour=ax.contourf(x,y,z,cmap='hot',levels=levels,vmin=z_min,vmax=z_max)
    fig.colorbar(contour,ax=ax,shrink=0.75,aspect=15,label='temperature',ticks=np.linspace(z_min,z_max,10+1),extend="max",location="right")

    

    print('Starting Render \n')
    start_time = time.time()
    with writer.saving(fig, "exp3d8.gif", 100):
        for t in np.linspace(0,time_play,nframes):
            z=func(x,y,t)
            name=f'Ring temperature over time: t={t:.2f}'
            contour=ax.contourf(x,y,z,cmap='hot',levels=levels,vmin=z_min,vmax=z_max)
            ax.set_title(name)
            ax.set_aspect(1)
            writer.grab_frame()
            plt.cla()
            progress_bar(t,time_play,start_time)
    print( '\n Contour animation Rendered' )
anim_3d_contour2()
# time_play=0.5
# nframes=round(time_play*frame_fps)+1
# print(f'fps = {frame_fps}, t = {time_play}, nfrm = {nframes}')
# print(np.linspace(0,time_play,nframes))

def anim_3d_3dplot():

    with writer.saving(fig, "exp3d3.gif", 100):
        for t in np.linspace(0,time_play,nframes):
            pass
    def func(x,y,r,t):
        # return np.cos(r/2+t)*np.exp(-np.square(r)/50)
        return np.sin(x)*np.cos(y)*np.sin(t)

    fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

    xvec = np.linspace(-10, 10, 1000)
    yvec = np.linspace(-10, 10, 1000)

    xlist, ylist = np.meshgrid(xvec, yvec)

    rlist = np.sqrt( np.square(xlist) + np.square(ylist) )
    levels = np.linspace(0, 1, 101)

    time_play=20
    frames=time_play*frame_fps
    start_time = time.time()
    with writer.saving(fig, "exp3d3.gif", 100):
        for tval in np.linspace(0,time_play,frames):
            # print(tval)
            zval = func(xlist,ylist,rlist, tval)
            ax.set_ylim(-5,5)
            ax.set_xlim(-5,5)
            ax.set_zlim(-1,1)
            ax.plot_surface(xlist,ylist,zval,cmap=cm.inferno)
            # plt.show()
            # plt.cla()
            writer.grab_frame()
            plt.cla()
            progress_bar(tval,time_play,start_time)
    print()
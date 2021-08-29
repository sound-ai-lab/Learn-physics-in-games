import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from IPython.display import HTML
from matplotlib.animation import FuncAnimation

flames = 100

fig, ax = plt.subplots(figsize=(16, 9))
image_path = "img/red_stop-0.png"
image = plt.imread(image_path)
im = OffsetImage(image, zoom=3)

r_start = (0, 3)
artists = []
red_x = [r_start[0]]
red_y = [r_start[1]]
# ln, = plt.plot(x, y, 'r', animated=True)
annotation = AnnotationBbox(im, (red_x[0], red_y[0]), xycoords='data', frameon=False)
artists.append(ax.add_artist(annotation))


def update(i):
    ax.clear()
    ax.set_xlim(-10, 50)
    ax.set_ylim(0, 20)
    ax.set_xlabel('x', fontsize=16)
    ax.set_ylabel('y', fontsize=16)
    ax.set_aspect('equal')

    ti = round(i / 10, 1)
    xi = 0
    yi = r_start[1]

    red_x.append(xi)
    red_y.append(yi)

    artists.append(ax.add_artist(annotation))
    annotation.xybox = (xi, yi)
    ax.set_title(f'T={ti:5} [sec] XY=({xi:6},{yi:6}) [m]  ')


ani = FuncAnimation(fig, update, frames=flames+1,
                    interval=100, blit=False)

HTML(ani.to_html5_video())

dpi = 100
ani.save('mp4/01.stop.mp4', writer="ffmpeg", dpi=dpi)

import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from IPython.display import HTML
from matplotlib.animation import FuncAnimation

v = 10  # [m/s]

goal = 50  # [m]
frames = int(round(50 / v * 100, 1)) + 1

fig, ax = plt.subplots(figsize=(16, 9))

image_path = []
image = []
im = []

for i in range(21):
    image_path.append("img/red_run-" + str(i) + ".png")
    image.append(plt.imread(image_path[i]))
    im.append(OffsetImage(image[i], zoom=3))

r_start = (0, 3)
artists = []


def update(i):
    ax.clear()
    ax.set_xlim(-10, goal + 10)
    ax.set_ylim(0, 20)
    ax.set_aspect('equal')
    ax.set_xlabel('x [m]', fontsize=16)
    ax.set_ylabel('y [m]', fontsize=16)

    ti = round(i / 100, 1)
    xi = round(r_start[0] + v * i / 100, 1)
    yi = round(r_start[1])

    # change moving flame
    c = int(round(xi * 2, 0))

    if xi * 100 < 21:
        annotation = AnnotationBbox(im[c], (xi, yi), xycoords='data', frameon=False)
    elif i == frames - 1:
        annotation = AnnotationBbox(im[0], (xi, yi), xycoords='data', frameon=False)
    else:
        annotation = AnnotationBbox(im[c % 21], (xi, yi), xycoords='data', frameon=False)

    artists.append(ax.add_artist(annotation))

    ax.set_title(f'T={ti:5} [sec] XY=({xi:6},{yi:6}) [m]')


ani = FuncAnimation(fig, update, frames=frames, interval=10, blit=False)

HTML(ani.to_html5_video())

dpi = 100
ani.save('mp4/02.speed.mp4', writer="ffmpeg", dpi=dpi)

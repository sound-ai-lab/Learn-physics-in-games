import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from IPython.display import HTML
from matplotlib.animation import FuncAnimation

v = 5  # [m/s]

goal = 50  # [m]
flames = int(50 / v) * 100

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
red_x = [r_start[0]]
red_y = [r_start[1]]


def update(i):
    ax.clear()
    ax.set_xlim(-10, goal + 10)
    ax.set_ylim(0, 20)
    ax.set_aspect('equal')
    ax.set_xlabel('x [m]', fontsize=16)
    ax.set_ylabel('y [m]', fontsize=16)

    t = round(i / 100, 1)

    xi = round(r_start[0] + v * i / 100, 1)
    yi = round(r_start[1])

    red_x.append(xi)
    red_y.append(yi)

    if i < 21:
        annotation = AnnotationBbox(im[i], (red_x[i], red_y[i]), xycoords='data', frameon=False)
    elif i == flames:
        t = round(goal / v, 1)
        xi = round(r_start[0] + goal, 1)
        yi = round(r_start[1])
        annotation = AnnotationBbox(im[0], (red_x[flames], red_y[flames]), xycoords='data', frameon=False)
    else:
        annotation = AnnotationBbox(im[i % 21], (red_x[i], red_y[i]), xycoords='data', frameon=False)

    artists.append(ax.add_artist(annotation))

    annotation.xybox = (xi, yi)
    ax.set_title(f'T={t:5} [sec] XY=({xi:6},{yi:6}) [sec]  ')


ani = FuncAnimation(fig, update, frames=flames + 1,
                    interval=10, blit=False)

HTML(ani.to_html5_video())

dpi = 100
ani.save('mp4/02.speed.mp4', writer="ffmpeg", dpi=dpi)
print("end")

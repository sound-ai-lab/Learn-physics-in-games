import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from IPython.display import HTML
from matplotlib.animation import FuncAnimation

v0 = 5  # [m/s]
a = 3  # [m/s2]

goal = 50  # [m]
frames = 600
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
goal_t = []
goal_x = []
goal_v = []


def update(i):
    ax.clear()
    ax.set_xlim(-10, goal + 10)
    ax.set_ylim(0, 20)
    ax.set_aspect('equal')
    ax.set_xlabel('x [m]', fontsize=16)
    ax.tick_params(labelleft=False, left=False)
    ti = round(i / 100, 1)

    vi = round(v0 + a * ti, 1)  # [m/s]

    xi = round(r_start[0] + v0 * i / 100 + 1 / 2 * a * (i / 100) ** 2, 1)
    yi = round(r_start[1])

    # change moving flame
    c = int(round(xi * 2, 0))

    if xi * 100 < 21:
        annotation = AnnotationBbox(im[c], (xi, yi), xycoords='data', frameon=False)
    elif goal <= xi:
        goal_t.append(ti)
        goal_x.append(xi)
        goal_v.append(vi)

        annotation = AnnotationBbox(im[0], (goal_x[0], yi), xycoords='data', frameon=False)
    else:
        annotation = AnnotationBbox(im[c % 21], (xi, yi), xycoords='data', frameon=False)

    artists.append(ax.add_artist(annotation))

    if goal <= xi:
        ax.set_title(f'a={a:5} [m/s2] T={goal_t[0]:5} [sec] X={goal_x[0]:6}[m],V={goal_v[0]:6}[m/s]')
    else:
        ax.set_title(f'a={a:5} [m/s2] V0={v0:5} [m/s] T={ti:5} [sec] X={xi:6}[m],V={vi:6}[m/s]')


ani = FuncAnimation(fig, update, frames=frames, interval=10, blit=False)

HTML(ani.to_html5_video())

dpi = 100
ani.save('mp4/02.acceleration.mp4', writer="ffmpeg", dpi=dpi)

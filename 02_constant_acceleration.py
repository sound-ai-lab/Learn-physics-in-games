import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from IPython.display import HTML
from matplotlib.animation import FuncAnimation

v0 = 5  # [m/s]
a = 2  # [m/s2]

goal = 50  # [m]
frames = 500

fig = plt.figure(figsize=(16, 9))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

image_path = []
image = []
im = []

for i in range(21):
    image_path.append("img/red_run-" + str(i) + ".png")
    image.append(plt.imread(image_path[i]))
    im.append(OffsetImage(image[i], zoom=3))

image_path = "img/blue_dot.png"
image = plt.imread(image_path)
im2 = OffsetImage(image, zoom=3)

r_start = (0, 3)

goal_t = []
goal_x = []
goal_v = []

ln_x = []
ln_y = []

for i in range(frames):
    ln_x.append(round(r_start[0] + v0 * i / 100 + 1 / 2 * a * (i / 100) ** 2, 1))
    ln_y.append(round(v0 + a * i / 100, 1))  # [m/s]


def update(i):
    ax1.clear()
    ax2.clear()
    ax1.set_xlim(-10, goal + 10)
    ax1.set_ylim(0, 20)
    ax1.set_aspect('equal')
    ax1.set_xlabel('x [m]', fontsize=16)
    ax1.tick_params(labelleft=False, left=False)

    ax2.set_xlim(-10, goal + 10)
    ax2.set_ylim(0, 20)
    ax2.set_aspect('equal')
    ax2.set_xlabel('x [m]', fontsize=16)
    ax2.set_ylabel('v [m/s]', fontsize=16)

    ti = round(i / 100, 1)

    vi = round(v0 + a * ti, 1)  # [m/s]

    xi = round(r_start[0] + v0 * i / 100 + 1 / 2 * a * (i / 100) ** 2, 1)
    yi = round(r_start[1])

    ax2.plot(ln_x, ln_y)


    # change moving flame
    c = int(round(xi * 2, 0))

    if xi * 100 < 21:
        annotation1 = AnnotationBbox(im[c], (xi, yi), xycoords='data', frameon=False)
        ax2.plot(xi, vi, color='red', linestyle='dashed', marker='o',
                 markerfacecolor='blue', markersize=12)
    elif goal <= xi:
        goal_t.append(ti)
        goal_x.append(xi)
        goal_v.append(vi)
        annotation1 = AnnotationBbox(im[0], (goal_x[0], yi), xycoords='data', frameon=False)
        ax2.plot(goal_x[0], goal_v[0], color='red', linestyle='dashed', marker='o',
                 markerfacecolor='red', markersize=12)
    else:
        annotation1 = AnnotationBbox(im[c % 21], (xi, yi), xycoords='data', frameon=False)
        ax2.plot(xi, vi, color='red', linestyle='dashed', marker='o',
                 markerfacecolor='red', markersize=12)

    ax1.add_artist(annotation1)

    if goal <= xi:
        ax1.set_title(f'a={a:5} [m/s2] T={goal_t[0]:5} [sec] X={goal_x[0]:6}[m],V={goal_v[0]:6}[m/s]')
    else:
        ax1.set_title(f'a={a:5} [m/s2] T={ti:5} [sec] X={xi:6}[m],V={vi:6}[m/s]')


ani = FuncAnimation(fig, update, frames=frames, interval=10, blit=False)

HTML(ani.to_html5_video())

dpi = 100
ani.save('mp4/02_constant_acceleration.mp4', writer="ffmpeg", dpi=dpi)

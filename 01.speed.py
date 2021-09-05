import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from IPython.display import HTML
from matplotlib.animation import FuncAnimation

v1 = 10  # [m/s]
v2 = 5

goal = 50  # [m]

if v1 < v2:
    frames = int(round(goal / v1 * 100, 1)) + 1
else:
    frames = int(round(goal / v2 * 100, 1)) + 1

fig, ax = plt.subplots(figsize=(16, 9))

image_path = []
image = []
im = []

image_path.append("img/red_stop-0.png")
image.append(plt.imread(image_path[0]))
im.append(OffsetImage(image[0], zoom=3))

for i in range(21):
    image_path.append("img/red_run-" + str(i) + ".png")
    image.append(plt.imread(image_path[i + 1]))
    im.append(OffsetImage(image[i + 1], zoom=3))

r1_start = (0, 3)
r2_start = (0, 10)
r3_start = (0, 17)


def update(i):
    ax.clear()
    ax.set_xlim(-10, goal + 10)
    ax.set_ylim(0, 20)
    ax.set_aspect('equal')
    ax.set_xlabel('x [m]', fontsize=16)
    ax.tick_params(labelleft=False, left=False)

    ti = round(i / 100, 1)
    xi1 = round(r1_start[0] + v1 * i / 100, 1)
    xi2 = round(r2_start[0] + v2 * i / 100, 1)
    yi1 = round(r1_start[1])
    yi2 = round(r2_start[1])

    # change moving flame
    c1 = int(round(xi1 * 2, 0))
    c2 = int(round(xi2 * 2, 0))

    if xi1 * 100 < 21:
        annotation1 = AnnotationBbox(im[c1], (xi1, yi1), xycoords='data', frameon=False)
    elif i == frames - 1 or goal <= xi1:
        xi1 = goal
        annotation1 = AnnotationBbox(im[0], (goal, yi1), xycoords='data', frameon=False)
    else:
        annotation1 = AnnotationBbox(im[c1 % 21], (xi1, yi1), xycoords='data', frameon=False)

    if xi2 * 100 < 21:
        annotation2 = AnnotationBbox(im[c2], (xi2, yi2), xycoords='data', frameon=False)
    elif i == frames - 1 or goal <= xi2:
        xi2 = goal
        annotation2 = AnnotationBbox(im[0], (goal, yi2), xycoords='data', frameon=False)
    else:
        annotation2 = AnnotationBbox(im[c2 % 21], (xi2, yi2), xycoords='data', frameon=False)

    annotation3 = AnnotationBbox(im[0], (0, r3_start[1]), xycoords='data', frameon=False)

    ax.add_artist(annotation1)
    ax.add_artist(annotation2)
    ax.add_artist(annotation3)

    ax.set_title(f'T={ti:5} [sec] X=({0:6},{xi2:6},{xi1:6}) [m]')


ani = FuncAnimation(fig, update, frames=frames, interval=10, blit=False)

HTML(ani.to_html5_video())

dpi = 100
ani.save('mp4/01.speed.mp4', writer="ffmpeg", dpi=dpi)

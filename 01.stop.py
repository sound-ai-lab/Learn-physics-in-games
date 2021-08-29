import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots(figsize=(16, 9))
image_path = "red_stop-0.png"
image = plt.imread(image_path)
im = OffsetImage(image, zoom=5)

red_start_pos = (0,12)
artists = []
red_x = [red_start_pos[0]]
red_y = [red_start_pos[1]]
# ln, = plt.plot(x, y, 'r', animated=True)
annotation = AnnotationBbox(im, (red_x[0], red_y[0]), xycoords='data', frameon=False)
artists.append(ax.add_artist(annotation))


def init():
    ax.set_xlim(-10, 200)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    # ax.patch.set_facecolor('gold')  # 図全体の背景色
    # ax.set_title(str(0))

def update(i):
    xi = 0
    yi = red_start_pos[1]
    red_x.append(xi)
    red_y.append(yi)
    # ln.set_data(xdata, ydata)
    annotation.xybox = (xi, yi)
    ax.set_title(str(i))
    # return ln, annotation


ani = FuncAnimation(fig, update, frames=100,
                    interval=100, init_func=init, blit=False)

HTML(ani.to_html5_video())

dpi = 100
ani.save('01.stop.mp4', writer="ffmpeg", dpi=dpi)

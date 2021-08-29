import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

flames = 500
push_flame = 50
steps = 10

# オブジェクトの生成
fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)

x1 = np.arange(0, flames - push_flame * 1 / steps, 1 / steps)
x1 = np.insert(x1, 0, np.zeros(push_flame))
y1 = np.zeros(int(500 * steps))

x2 = -np.ones(push_flame)
x2 = np.append(x2, np.full(int(flames * steps - push_flame), 0))
y2 = y1

print("x1", x1.shape)
print("y1", y1.shape)
print("x2", x2.shape)
print("y2", y2.shape)


# アニメーション更新用の関数
def update_func(i):
    # 前のフレームで描画されたグラフを消去
    ax.clear()

    ax.plot(x1[i], y1[i], color='red', marker='o', markersize=10)
    ax.plot(x2[i], y2[i], color='black', marker='o', markersize=10)
    # 軸ラベルの設定
    ax.set_xlabel('x[m]', fontsize=12)
    ax.set_ylabel('y[m]', fontsize=12)
    ax.set_xlim(-10, flames / steps)
    ax.set_ylim(-1, 4)
    # サブプロットタイトルの設定
    ax.set_title(str(i))


ani = animation.FuncAnimation(fig, update_func, frames=flames, interval=1, repeat=True)

# 表示
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

flames = 55
collision_flame = 5

# オブジェクトの生成
fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)

x1 = np.arange(0, flames, 1)
x1 = np.insert(x1, 0, np.zeros(collision_flame))
y1 = np.zeros(100)

x2 = np.arange(-collision_flame, 0, 1)
x2 = np.append(x2, np.full(flames - collision_flame,-1))
y2 = np.zeros(100)

# アニメーション更新用の関数
def update_func(i):
    # 前のフレームで描画されたグラフを消去
    ax.clear()

    # print("x=", i)
    # print("y=", y)
    # ax.plot(x, y, "b")
    ax.plot(x1[i], y1[i], color='red', marker='o', markersize=10)
    ax.plot(x2[i], y2[i], color='black', marker='o', markersize=10)
    # 軸ラベルの設定
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_xlim(-10, 50)
    ax.set_ylim(-1, 4)
    # サブプロットタイトルの設定
    ax.set_title(str(i))

ani = animation.FuncAnimation(fig, update_func, frames=flames, interval=200, repeat=False)

# 表示
plt.show()

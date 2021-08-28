import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# フィギュアオブジェクトの生成
fig = plt.figure()

# figure内にサブプロットを一つ配置
ax = fig.add_subplot(1, 1, 1)

x = np.arange(0, 10, 0.1)


# アニメーション更新用の関数
def update_func(i):
    # 前のフレームで描画されたグラフを消去
    ax.clear()

    y = 2 * np.sin(x - i)
    ax.plot(x, y, "b")
    # 軸ラベルの設定
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    # サブプロットタイトルの設定
    ax.set_title('Frame: ' + str(i))


ani = animation.FuncAnimation(fig, update_func, frames=10, interval=200, repeat=True)

# 表示
plt.show()

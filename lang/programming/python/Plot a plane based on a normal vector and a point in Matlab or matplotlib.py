from book_draw_util import *

# import mpl_toolkits.axisartist as axisartist
# import matplotlib.pyplot as plt


fig = plt.figure(figsize=(10, 6)) # width, height in inches.  1英寸=2.54厘米
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")


sigma = np.arange(-8, 8, 0.01)
ax.grid(True)
ax.plot(sigma, logistic(sigma), c="k")
plt.xlim(-8, 8)
plt.ylim(-.21, 1.2)
ax.text(x=8.5 , y=-0.02, s=r"$a$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.text(x=-1.2, y=1.3, s=r"$\mathrm{Logistic}\left(a\right)$", fontsize=AXIS_LABEL_FONT_SIZE)

plt.savefig(os.path.join("D:\workcode\python\plot\高品质图片", '1-1.png'), format='png', dpi=600)
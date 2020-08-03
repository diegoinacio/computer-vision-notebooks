import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as manim


def plot_function1(f):
	t = np.linspace(- np.pi, np.pi, 10)

	# visualization
	fig, ax = plt.subplots(1, 1)
	ax.plot(t, f(t), c='#FF0044')
	ax.plot(t*2, f(t)*2, ':', c='#FF0044')

	ax.scatter([-np.pi, np.pi], [-1, 1], marker='o', s=100, c='#FF0044')
	ax.set_xlim([-4.2*np.pi, 4.2*np.pi])
	ax.set_ylim([-1.2, 1.2])
	ax.set_xticks([i*np.pi for i in range(-4, 5)])
	ax.set_yticks((-1, 0, 1))
	xlabels = [f'${i}\pi$' for i in range(-4, 5)]
	xlabels = list(map(lambda x: x.replace('1', ''), xlabels))
	xlabels[len(xlabels)//2] = '0'
	ax.set_xticklabels(xlabels)
	ax.set_yticklabels(['$-1$', '0', '$1$'])
	ax.grid(alpha=0.75, linestyle=':')
	ax.axhline(y=0, color='k', alpha=0.5)
	ax.axvline(x=0, color='k', alpha=0.5)

	plt.show()


def plot_function2(f):
	t = np.linspace(- np.pi, np.pi, 100)

	# visualization
	fig, ax = plt.subplots(1, 1)
	ax.plot(t, f(t), c='#44AA00')
	ax.plot(t*2, f(t*2), ':', c='#44AA00')

	ax.scatter([-np.pi, np.pi], [np.pi**2, np.pi**2], marker='o', s=100, c='#44AA00')
	ax.set_xlim([-4.2*np.pi, 4.2*np.pi])
	ax.set_ylim([-0.5, np.pi**2 + 0.5])
	ax.set_xticks([i*np.pi for i in range(-4, 5)])
	ax.set_yticks([i*np.pi for i in range(4)])
	xlabels = [f'${i}\pi$' for i in range(-4, 5)]
	xlabels = list(map(lambda x: x.replace('1', ''), xlabels))
	xlabels[len(xlabels)//2] = '0'
	ax.set_xticklabels(xlabels)
	ylabels = [f'${i}\pi$' for i in range(4)]
	ylabels = list(map(lambda x: x.replace('1', ''), ylabels))
	ylabels[0] = '0'
	ax.set_yticklabels(ylabels)
	ax.grid(alpha=0.75, linestyle=':')
	ax.axhline(y=0, color='k', alpha=0.5)
	ax.axvline(x=0, color='k', alpha=0.5)

	plt.show()


def periodic_function1(f):
	t = np.linspace(- np.pi, np.pi, 10)

	# visualization
	fig, ax = plt.subplots(1, 1)

	for i in range(5):
		to = - 4*np.pi + 2*np.pi*i
		l = ax.plot(t + to, f(t), c='#FF0044', zorder=1)[0]
		ax.scatter([
			to - np.pi, to + np.pi], [-1, 1],
			marker='o', s=100, zorder=2,
			facecolor="white",
			edgecolor=l.get_color(),
			linewidth=l.get_linewidth()
		)

	ax.scatter([i*np.pi for i in range(-3, 4, 2)], [0]*4, marker='o', s=100, zorder=8, c='#FF0044')
	ax.set_xlim([-4.2*np.pi, 4.2*np.pi])
	ax.set_ylim([-1.2, 1.2])
	ax.set_xticks([i*np.pi for i in range(-4, 5)])
	ax.set_yticks((-1, 0, 1))
	xlabels = [f'${i}\pi$' for i in range(-4, 5)]
	xlabels = list(map(lambda x: x.replace('1', ''), xlabels))
	xlabels[len(xlabels)//2] = '0'
	ax.set_xticklabels(xlabels)
	ax.set_yticklabels(['$-1$', '0', '$1$'])
	ax.grid(alpha=0.75, linestyle=':')
	ax.axhline(y=0, color='k', alpha=0.5)
	ax.axvline(x=0, color='k', alpha=0.5)

	plt.show()


def periodic_function2(f):
	t = np.linspace(- np.pi, np.pi, 100)

	# visualization
	fig, ax = plt.subplots(1, 1)

	for i in range(5):
		to = - 4*np.pi + 2*np.pi*i
		ax.plot(t + to, f(t), c='#44AA00', zorder=1)[0]

	ax.set_xlim([-4.2*np.pi, 4.2*np.pi])
	ax.set_ylim([-0.5, np.pi**2 + 0.5])
	ax.set_xticks([i*np.pi for i in range(-4, 5)])
	ax.set_yticks([i*np.pi for i in range(4)])
	xlabels = [f'${i}\pi$' for i in range(-4, 5)]
	xlabels = list(map(lambda x: x.replace('1', ''), xlabels))
	xlabels[len(xlabels)//2] = '0'
	ax.set_xticklabels(xlabels)
	ylabels = [f'${i}\pi$' for i in range(4)]
	ylabels = list(map(lambda x: x.replace('1', ''), ylabels))
	ylabels[0] = '0'
	ax.set_yticklabels(ylabels)
	ax.grid(alpha=0.75, linestyle=':')
	ax.axhline(y=0, color='k', alpha=0.5)
	ax.axvline(x=0, color='k', alpha=0.5)

	plt.show()


def serie_function1(s):
	t = np.linspace(- 5*np.pi, 5*np.pi, 4410)

	# visualization
	fig, ax = plt.subplots(1, 1)

	ax.plot(t, s(t), c='#FF0044')
	ax.set_xlim([-4.2*np.pi, 4.2*np.pi])
	ax.set_ylim([-1.2, 1.2])
	ax.set_xticks([i*np.pi for i in range(-4, 5)])
	ax.set_yticks((-1, 0, 1))
	xlabels = [f'${i}\pi$' for i in range(-4, 5)]
	xlabels = list(map(lambda x: x.replace('1', ''), xlabels))
	xlabels[len(xlabels)//2] = '0'
	ax.set_xticklabels(xlabels)
	ax.set_yticklabels(['$-1$', '0', '$1$'])
	ax.grid(alpha=0.75, linestyle=':')
	ax.axhline(y=0, color='k', alpha=0.5)
	ax.axvline(x=0, color='k', alpha=0.5)

	plt.show()


def serie_function2(s):
	t = np.linspace(- 5*np.pi, 5*np.pi, 4410)

	# visualization
	fig, ax = plt.subplots(1, 1)

	ax.plot(t, s(t), c='#44AA00')
	ax.set_xlim([-4.2*np.pi, 4.2*np.pi])
	ax.set_ylim([-0.5, np.pi**2 + 0.5])
	ax.set_xticks([i*np.pi for i in range(-4, 5)])
	ax.set_yticks([i*np.pi for i in range(4)])
	xlabels = [f'${i}\pi$' for i in range(-4, 5)]
	xlabels = list(map(lambda x: x.replace('1', ''), xlabels))
	xlabels[len(xlabels)//2] = '0'
	ax.set_xticklabels(xlabels)
	ylabels = [f'${i}\pi$' for i in range(4)]
	ylabels = list(map(lambda x: x.replace('1', ''), ylabels))
	ylabels[0] = '0'
	ax.set_yticklabels(ylabels)
	ax.grid(alpha=0.75, linestyle=':')
	ax.axhline(y=0, color='k', alpha=0.5)
	ax.axvline(x=0, color='k', alpha=0.5)

	plt.show()

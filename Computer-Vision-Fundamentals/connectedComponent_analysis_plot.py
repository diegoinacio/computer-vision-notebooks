import matplotlib.pyplot as plt

def visualize_grid(grid, grid_labeld, subsets):
	N, M = len(grid), len(grid[0])

	fig, (axA, axB) = plt.subplots(1, 2, figsize=(20,10))

	axA.imshow(grid, cmap="gray")
	axA.set_title("Input grid")

	axB.imshow(grid_labeld)
	for n in range(N):
		for m in range(M):
			if grid_labeld[n][m] <= 0:
				continue
			axB.text(
				m, n, f'{grid_labeld[n][m]}',
				color='w', size=24,
				horizontalalignment='center',
				verticalalignment='center'
			)
	axB.set_title(f'Connected-component subsets | Total: {subsets}')


	plt.show()

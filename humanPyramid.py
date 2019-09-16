#%%
from time import perf_counter 


def weightOn(row, column, weight = 200):
	if row == 0:
		return 0.00
	elif column == 0:
		newWeight = (weightOn(row-1, column, weight) + weight) / 2
		return newWeight
	elif column == row:
		newWeight = (weightOn(row - 1, column - 1, weight) + weight) / 2
		return newWeight
	else:
		newWeight = (weight + (weightOn(row - 1, column - 1, weight)/2) + (weightOn(row - 1, column, weight)) / 2)
		return newWeight



def main(pyramidHeight):
	t1_start = perf_counter()  
	rowCount = 0
	cache = {}
	while rowCount < pyramidHeight:
		columnCount = 0
		if rowCount <= pyramidHeight:
			rowWeights = []
			while columnCount <= rowCount:
				if (rowCount, columnCount) in cache.keys():
					# print('Test ' + str(cache[(rowCount,columnCount)]))
					rowWeights.append(f"{cache[(rowCount,columnCount)]:.2f}")
					columnCount += 1
				else:
					indWeight = weightOn(rowCount, columnCount)
					rowWeights.append(f"{indWeight:.2f}")
					columnCount += 1
					cache[(rowCount, columnCount)] = indWeight
			print(rowWeights)
		rowCount += 1
	t1_stop = perf_counter()  
	print(f"Elapsed Time: {t1_stop-t1_start} seconds")
	# print(cache)

	



main(23)
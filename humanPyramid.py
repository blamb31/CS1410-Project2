#%%
from time import perf_counter 
import sys

cache = {}

def weightOn(row, column, weight = 200):
	if row == 0:
		return 0.00
	elif column == 0:
		if (row, column) in cache.keys():
			return cache[(row,column)]
		else:
			newWeight = (weightOn(row-1, column, weight) + weight) / 2
			cache[(row,column)] = newWeight
			return newWeight
	elif column == row:
		if (row, column) in cache.keys():
			return cache[(row,column)]
		else:
			newWeight = (weightOn(row - 1, column - 1, weight) + weight) / 2
			cache[(row,column)] = newWeight			
			return newWeight
	else:
		if (row, column) in cache.keys():
			return cache[(row,column)]
		else:
			newWeight = (weight + (weightOn(row - 1, column - 1, weight)/2) + (weightOn(row - 1, column, weight)) / 2)
			cache[(row,column)] = newWeight						
			return newWeight



def main(pyramidHeight):
	t1_start = perf_counter()  
	rowCount = 0
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
			space = ' '
			rowWeightsString = space.join(rowWeights)
			print(rowWeightsString)
		rowCount += 1
	t1_stop = perf_counter()  
	print(f"Elapsed Time: {t1_stop-t1_start} seconds")
	# print(cache)

	


if __name__== "__main__" :
	main(int(sys.argv[1]))

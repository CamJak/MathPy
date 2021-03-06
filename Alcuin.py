import numpy as np


# generate footprint matrix from given matrix
def footprint_gen(graph):
	footprint_matrix = graph[:,0]
	cur_row = 0
	for row in graph:
		total = 0
		for item in row:
			total += item
		
		footprint_matrix[cur_row] = total
		cur_row += 1
		
	# sorts matrix in increasing order
	footprint_matrix = np.sort(footprint_matrix)
	
	return footprint_matrix

 
# create 3x3 identity matrix (this is a blank graph)
graph3x3 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(graph3x3)

# generate footprint and print it
out = footprint_gen(graph3x3)
print(out)

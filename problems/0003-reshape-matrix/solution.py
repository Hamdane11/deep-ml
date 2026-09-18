import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	x = np.array(a)
	if x.size != new_shape[0] * new_shape[1] :
		return []
	else:

		temp = x.reshape((new_shape))

		return temp.tolist()






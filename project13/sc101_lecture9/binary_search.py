def main():
	lst = [3, 6, 9, 10, 11, 23, 33, 45, 66, 99]
	print(binary_search(lst, 7))
	print(binary_search(lst, 23))


def binary_search(lst, target):
	"""
	:param lst: list[int], a Python list storing integers.
	:param target: int, the value to be searched.
	:returns : bool, if target is in the lst or not.
	"""
	# Your Code Here
	left_p, right_p = 0, len(lst)
	while True:
		mid = (left_p + right_p) // 2
		if target == lst[mid]:
			return True
		elif target > lst[mid]:
			left_p = mid + 1
		else:
			right_p = mid - 1
		if left_p == right_p:
			return False



if __name__ == '__main__':
	main()

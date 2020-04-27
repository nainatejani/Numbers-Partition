


# def partition(S):
# 	i = 0
# 	length = len(S)

# 	def recursive_partition(i):
# 		if i == length:


# 		element_included = res += S[i]
# 		element_not_included = res

def arrSum(S, i, addition, sol = []):
	print(sol)
	print(addition)
	if (addition == 0):
		print("I am here" + str(sol))
		return sol

	elif (i < 0 or addition < 0):
		return

	# ith term included
	# print(str(S[i]) + "S[" + str(i) + "]th term here")
	# print(str(sol) + "here")
	ith_included = arrSum(S, i - 1, addition - S[i], sol + [S[i]])
	# ith term not included
	ith_not_included = arrSum(S, i - 1, addition, sol)
	print(str(ith_included)+"ith included")

	if ith_included:
		print("I am here")
		return ith_included
	elif ith_not_included:
		return ith_not_included

	return ith_included

print(arrSum([10,8,7,6,5], 1, 18))

def arrSum(S, i, addition):
	T = [[]]

	length = len(S)

	for i in range(addition):
		T[0].append([])
	for i in range(length):
		T[i][0] = []
	for i in range(length):
		for j in range(addition):
			if S[i-1] > j:
				T[i][j] = T[i-1][j]





















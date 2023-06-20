def solve(lst):
	if len(lst) == 0:
		return None
	return find_max(0, len(lst)-1, lst)

def find_max(start, end, lst):
	if start == end:
		return lst[start]
	mid = (start + end) // 2
	return max(
		find_max(start, mid, lst),
		find_max(mid+1, end, lst)
	)


lst = [int(val) for val in input().split()]
print(solve(lst))


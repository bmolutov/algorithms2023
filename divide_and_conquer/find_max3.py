from math import ceil


def solve(lst):
	if not lst:
		return None
	return find_max3(0, len(lst)-1, lst)



"""
      *     * 
1 2 3 4 5 6 7 8 9

(0 + 8) // 3
0 -> 3 -> 6...

inc = (start + end) // 3
mid1 = start + inc
mid2 = mid1 + inc

[start; mid1) [mid1; mid2) [mid2; end]

1 2
inc = (0 + 1) // 3 -> 1

mid1 = 1
mid2 = 2

0 -> 0
1 

"""
def find_max3(start, end, lst):
	if end - start == 0:
		return lst[start]
	if end - start == 1:
		return max(lst[start], lst[start+1]) 
	if end - start == 2:
		return max(lst[start], lst[start+1], lst[start+2])
	
	inc = int(ceil((start + end) / 3))
	mid1 = start + inc
	mid2 = mid1 + inc

	return max(
		find_max3(start, mid1-1, lst),
		find_max3(mid1, mid2-1, lst),
		find_max3(mid2, end, lst)
	)


lst = [int(val) for val in input().split()]
print(solve(lst))


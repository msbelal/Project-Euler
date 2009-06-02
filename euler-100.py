import quadratic

"""
6 15 [2, 3] [3, 5]
35 85 [5, 7] [5, 17]
204 493 [2, 2, 3, 17] [17, 29]
1189 2871 [29, 41] [3, 3, 11, 29]
6930 16731 [2, 3, 3, 5, 7, 11] [3, 3, 11, 13, 13]
40391 97513 [13, 13, 239] [13, 13, 577]
235416 568345 [2, 2, 2, 3, 17, 577] [5, 197, 577]
1372105 3312555 [5, 7, 197, 199] [3, 5, 19, 59, 197]
7997214 19306983 [2, 3, 19, 29, 41, 59] [3, 19, 59, 5741]
"""

p = [1, 6, 35, 204]

while 1 :
	r = (6 * p[-1]) - p[-2]
	c = -(r * (r - 1))
	b = -(1 + 2*r)
	a = 1
	t = quadratic.quadratic(a,b,c)
	best_root = t[0]
	if int(best_root) == best_root :
		best_root = int(best_root)
		print r, best_root
		p.append(r)
	if (r + best_root) > 1000*1000*1000*1000 :
		print r, best_root, r + best_root
		break
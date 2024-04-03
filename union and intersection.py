def main ():
	set_A = set({1, 2, "hello"})
	set_B = set({2, 3, 10})

	set_intersection = set_A.intersection(set_B)
	print(set_intersection)
	set_intersection= set_A.union(set_B)
	print(set_intersection)
main ()

def raise_to(exp):
	def raise_to_exp(x):
		return pow(x, exp)
	return raise_to_exp

raise_to_two = raise_to(2)

assert raise_to_two(3) == 9

raise_to_three = raise_to(3)

assert raise_to_three(2) == 8

import random

def get_randomprime():
	with open('primes1024.txt', 'r') as file:
		for num, aline in enumerate(file, 2):
	  		if random.randrange(num): continue
	  		line = aline
		return line

print(get_randomprime())
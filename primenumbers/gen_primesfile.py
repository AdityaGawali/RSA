from Crypto.Util import number

n_length = 1024
for i in range(1000):
	primeNum = number.getPrime(n_length)
	with open('primes1024.txt', 'a') as file:
		file.write(str(primeNum)+"\n")
	print(i)



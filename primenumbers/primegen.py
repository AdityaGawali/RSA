from random import randint

def is_prime(num, test_count):
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True

def generate_big_prime(n):
    found_prime = False
    while not found_prime:
        p = randint(2**(n-1), 2**n)
        if is_prime(p, 1000):
            return p
append=0
while True:
    nbit = int(input("Enter the bit "))
    if(append==0):
        file = open("primenumbers.txt","w")
    elif(append==1):
        file = open("primenumbers.txt","a")
    primeNumber1=generate_big_prime(nbit)
    primeNumber2=generate_big_prime(nbit)
    file.write(str(primeNumber1))
    file.write("\n")
    file.write(str(primeNumber2))
    file.write("\n")
    file.write(str(primeNumber1*primeNumber2))
    file.write("\n")
    append=1
from random import randint

def isPrime(num, test_count): #Checks whether number is prime
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True

def generatePrimeNumber(n): #Generates random prime number upto n bits 
    found_prime = False
    while not found_prime:
        p = randint(2**(n-1), 2**n)
        if isPrime(p, 1000):
            return p

def productOfPrimeNumber(primeNumber1,primeNumber2): #Calculates PublicKey1(N) = P1*P2
    N=primeNumber1*primeNumber2
    return N

def Phi(primeNumber1,primeNumber2): #Calculates Phi(N) for prime numbers
    return ((primeNumber1-1)*(primeNumber2-1))

def generatePublicKeyExponent(PHIofN): #Generates PublicKey2 EncryptionExponent(E)
    if(PHIofN % 3 != 0):
        E=3
    elif((PHIofN % 5 != 0)):
        E=5
    elif((PHIofN % 7 != 0)):
        E=7
    return E

def generatePrivateKey(K,phiofn,publicexp): #Generates PrivateKey(D) for decryption
    D = (K*(phiofn)+1)/publicexp
    return D

# def writePublicKey(num,exp,privateDecryptionKey): #write public key
#     publicKeyFile = open("publickey.txt","w")
#     publicKeyFile.write(str(num))
#     publicKeyFile.write("\n")
#     publicKeyFile.write(str(exp))
#     publicKeyFile.write("\n")
#     publicKeyFile.write(str(privateDecryptionKey))
#     publicKeyFile.close()




# def readCipher(): #read ciphertext 
#     publicKeyFile=open("publickey.txt","r")
#     publicKeyFile.readline() 
#     publicKeyFile.readline()
#     privateDecryptionKey = publicKeyFile.readline()
#     publicKeyFile.close()
#     cipherfile = open("cipher.txt","r")
#     cipherText = cipherfile.readline()
#     return cipherText


def readMessageText():
    messagefile = open("message.txt",'r')
    messageText = messagefile.readline()
    messagefile.close()
    return messageText

def ConvertInttoString(someInt): #convert int list to string text
    somelist=[chr(x) for x in someInt]
    someText = "".join(somelist)
    return someText

def ConvertStringtoInt(someText): #convert string text to int list
    somelist = list(someText)
    someInt = [ord(x) for x in somelist]
    return someInt  

def encrypt(messageText,primeProduct,publicExponentKey):
    cipherInt=[]
    messageInt = ConvertStringtoInt(messageText)
    for x in range(len(messageInt)):
        cipherInt = ((messageInt**publicExponentKey)%primeProduct)
    cipherText = ConvertInttoString(cipherInt)
    return cipherText

def decrypt(cipherText,primeProduct,privateDecryptionKey):
    cipherInt = ConvertStringtoInt(cipherText)
    decryptedMessageInt=[]
    for x in range(len(cipherInt)):
        decryptedMessageInt[x] = ((cipherInt[x]**privateDecryptionKey)%primeProduct)
    decryptedMessageText = ConvertInttoString(decryptedMessageInt)
    return decryptedMessageText
    

#MAIN CODE STARTS HERE
primeNumber1 = generatePrimeNumber(128)
primeNumber2 = generatePrimeNumber(128)
primeProduct = productOfPrimeNumber(primeNumber1,primeNumber2)
PHIIofN = Phi(primeNumber1,primeNumber1)
publicExponentKey = generatePublicKeyExponent(PHIIofN)
privateDecryptionKey = generatePrivateKey(2,PHIIofN,publicExponentKey)

messageText=readMessageText()
CipherText = encrypt(messageText,primeProduct,publicExponentKey)
decryptedMessageText = decrypt(CipherText,primeProduct,privateDecryptionKey)

final = open("final.txt","w")
final.write(CipherText)
final.write("\n")
final.write(decryptedMessageText)
print(decryptedMessageText)
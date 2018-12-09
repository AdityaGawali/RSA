def Encrypt(messageInt,N,publicExponent): # Encryption algo
    cipherInt=[]
    for x in messageInt:
        cipherInt[x] = (messageInt[x]**publicExponent)%N    
    return cipherInt

def ConvertInttoString(cipherInt): #convert int list to string
    cipherlist=[chr(x) for x in cipherInt]
    cipherText = "".join(cipherlist)
    return cipherText

def ConvertStringtoInt(messageText): ##convert string to intlist
    messagelist = list(messageText)
    messageInt = [ord(x) for x in messagelist]
    return messageInt

def readMessage(): #read message text
    message = open("message.txt","r")
    messageText = message.readline()
    message.close()

def readPublicKey(): #read public key
    publicKey = open("publickey.txt","r")
    N = publicKey.readline()
    publicExponent = publicKey.readline()
    publicKey.close()

def writeCiphertext(cipherText): #write cipher text
    cipherfile = open("cipher.txt","w")
    cipherfile.write(cipherText)
    cipherfile.close()

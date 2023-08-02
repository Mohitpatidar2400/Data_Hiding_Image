


letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",",",".","!","?"," ","A","B","C","D","E","F","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","10","G"]
number = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68"]
    

def gcd(a, b):
    while b != 0:
        (a, b)=(b, a % b)
    return a

def cale(n):
    
    for k in range(2, n ):
        if gcd(n, k) == 1:
            return k

def phii(a,b):
    g=(a-1)*(b-1)
    return g


def inverse(phi,e):
    for i in range(1,phi+1):
        if(((i*e)%phi)==1):
            return i




def cipher(num,e):
    for i in range(len(num)):
        X.append((int(num[i])**e)%n)

def decipher(num,d):
    for i in range(len(num)):
        Y.append((int(num[i])**d)%n)


p=int(input("Enter a Prime Number: "))
q=int(input("Enter a Prime Number: "))
n=p*q
print("n",n)

phi=phii(p,q)
print("phi(n)",phi)
e=cale(phi)
print("Public Key",e,n)
d=inverse(phi,e)
print("Private Key",d,n)








def rsaEncryption(filePath):
  with open(filePath) as f:
    message=f.read()
   
    

    global plaintext, numC, j, X
    X=[]
    
    plaintext = (message)
    
    numC = []
    for i in range(len(plaintext)):
        for j in range(len(letter)):
            if(plaintext[i]==letter[j]):
                numC.append(number[j])
    
    cipher(numC,e)
    print("Ciphertext:", X)
    print("Number of Ciphertext blocks:", len(X))
    return X
    





# Decryption file data using RSA Algo
def rsaDecryption(msg):
    
    global i,j,Y
    Y=[]
    decipher(msg,d)
    numD=[]
    for i in range(len(Y)):
        for j in range(len(number)):
            if(Y[i]==int(number[j])):
                numD.append(letter[j])
    

    
    return numD









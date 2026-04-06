# This file contains all the important functions required for the sha-256 implementaion

# Imlpementing the preprocess function
def preprocess(message):
    #converting the message into bytes
    bytes_message = bytearray(message.encode("utf-8"))

    #padding
    l = len(bytes_message)*8 #---> the number of bits in the original message
    #adding one to the bytes_message but as we are working in bytes we will have to append 1000000
    bytes_message.append(0x80)
    k = (512-l-1-64-7 ) % 512 #---> the number of zeros
    while len(bytes_message) % 64 != 56:
        bytes_message.append(0x00)

    #64 bit representation of l
    L = l.to_bytes(8, byteorder="big")
    bytes_message.extend(L)
    #return bytes_message

    return bytes_message
    #parsing into blocks


#implementing the ROTR^n(X) function
def ROTnX(n,x):
    return SHRnX(n,x) | SHLnX(32-n, x)
#implementing the standard right shift function
def SHRnX(n,x):
    return x>>n & 0xFFFFFFFF

def SHLnX(n,x):
    return x<<n & 0xFFFFFFFF
#implementing the little sigma 1 function
def little_sigma1 (x):
    return (ROTnX(7,x)^ROTnX(18,x)^SHRnX(3,x)) & 0xFFFFFFFF

#implementing little sigma 2 function
def little_sigma2 (x):
    return (ROTnX(17,x)^ROTnX(19,x)^SHRnX(10,x)) & 0xFFFFFFFF

# choice function
def ch(x,y,z):
    return ((x&y)^(~x&z)) & 0xFFFFFFFF

# majority function
def maj(x,y,z):
    return ((x&y)^(x&z)^(y&z))&0xFFFFFFFF

# Big_sigma1
def Big_sigma1(x):
    return ROTnX(2,x)^ROTnX(13,x)^ROTnX(22,x)

# Big_sigma2
def Big_sigma2(x):
    return ROTnX(6,x)^ROTnX(11,x)^ROTnX(25,x)

# creating the constants K set and the set H
def fractional_part(x):
    return x - int(x)

def is_prime(x):
    sq_root1 = int(x**(1/2))
    for i in range(sq_root1):
        if i >=1 :
            if x%(i+1) == 0:
                return False
    return True

i = 2
count1 = 0
newlist = []
while count1 < 64:
    if is_prime(i):
        newlist.append(i)
        count1+=1
        i+=1
    else:
        i+=1

j = 2
count2 = 0
newlist2 = []
while count2 < 8:
    if is_prime(j):
        newlist2.append(j)
        j+=1
        count2+=1
    else:
        j+=1

#setting the set K of constants
K = []
for x in newlist:
    K.append(int(fractional_part(x**(1/3))*(2**32)))


#setting the initial hash values
H_constants = []
for x in newlist2:
    H_constants.append(int(fractional_part(x**(1/2))*(2**32)))

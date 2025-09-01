
import random
import math

def prime(start, end):
    found = False
    while found == False:
        num = random.randint(start, end)
        found = True
        for i in range(2, num-1):
            if num % i == 0:
                found = False
                break
    return num


# p = prime(2, 50)
p = 11

# q = prime(60, 100)
q = 13

n = p * q

lambda_n = (p - 1) * (q - 1)

e_found = False
while e_found == False:
    # e = random.randint(2, lambda_n)
    e = 7
    e_found = True
    if(math.gcd(e,lambda_n) != 1):
        e_found = False
             
print(e)

for i in range(1,lambda_n):
    if(((e%lambda_n)*(i%lambda_n) % lambda_n) == 1):
         d = i

print(d)

input_message = input("Enter a message: ")

# cipher = ""

# for i in input_message:
#     value = (ord(i) ** e) % n
#     cipher = cipher + chr(value)

cipher = input_message
print("Cipher", cipher)
decrypt = ""
for j in cipher:
    value = (ord(j) ** d) % n
    decrypt = decrypt + chr(value)

print("Decrypt", decrypt)
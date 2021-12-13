import random
from random import randint

password = ""
for i in range(5):
    i = chr(random.randint(65,90))
    for j in range (5):
        j = chr(random.randint(65,90)).lower()
        k = random.randint(0,9)
        password = str(password)+i+j+str(k)
print(password)

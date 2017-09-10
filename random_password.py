import random 
import string

Data_set = string.ascii_letters + string.digits 
password = random.choice(Data_set)

for x in range(0, 8): 
	password = password + random.choice(Data_set) 

print(password)
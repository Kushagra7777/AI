import random

list = []
for i in range(16):
    t = input('Enter: ')
    list.append(t)

for i in range(16):
    k = random.choice(list)
    print(i+1,k)    
    list.remove(k)
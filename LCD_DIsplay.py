import numpy as np 
'''
num = int(input())
h, v = "-", "|"
h_bars = np.array([])
'''

s = int(input())

m = np.zeros(((2 * s) + 3, s + 2), dtype=int)

#m[0,1], m[0,2], m[3,1], m[3,2], m[6,1], m[6,2] = "2"

#Conditions for Number 1




#Conditions for Number 2
for x in range(0,((2* (s+1)) + 1),(s+1)):
    m[x] = 1
    m[x,0] = 0
    m[x,-1] = 0

for y in range(1, s+1):
    m[y,-1] = 1

for z in range(s+2 , (((2 * s) + 3) - 1)):
    m[z,0] = 1

print(m)


import numpy as np
s = int(input())
m = np.zeros(((2 * s) + 3, s + 2), dtype=int)

#For Number 1
m[3,-1], m[1,-1] = 1, 1

#For Number 2
m[0,1] , m[1,-1], m[2,1], m[3,0], m[4,1] = 1, 1, 1, 1, 1

#For Number 3
m[0,1] , m[1,-1], m[2,1], m[3,2], m[4,1] = 1, 1, 1, 1, 1

#For Number 4
m[1,0] , m[1,-1], m[2,1], m[3,2] = 1, 1, 1, 1

#For Number 5
m[0,1] , m[1,0], m[2,1], m[3,-1], m[4,1] = 1, 1, 1, 1, 1

#For Number 6
m[0,1] , m[1,0], m[2,1], m[3,0], m[3,-1], m[4,1] = 1, 1, 1, 1, 1, 1

#For Number 7
m[0,1], m[1,-1], m[3,-1] = 1, 1, 1

#For Number 8
m[0,1] , m[1,0], m[1,-1], m[2,1], m[3,0], m[3, -1], m[4,1] = 1, 1, 1, 1, 1, 1, 1

#For Number 9
m[0,1] , m[1,0], m[1,-1], m[2,1], m[3, -1], m[4,1] = 1, 1, 1, 1, 1, 1

print(m)
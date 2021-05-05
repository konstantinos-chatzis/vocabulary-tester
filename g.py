tuple = {} 
tuple[(1,2,4)] = 8
tuple[(4,2,1)] = 10
tuple[(1,2)] = 12
_sum = 0
for k in tuple: 
    _sum += tuple[k] 
print(len(tuple) + _sum)
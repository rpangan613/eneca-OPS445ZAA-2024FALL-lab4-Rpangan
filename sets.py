#!/usr/bin/env python3
s1 = {'Prime', 'Ix', 'Secundus', 'Caladan'}
s2 = {1, 2, 3, 4, 5}
s3 = {4, 5, 6, 7, 8}


try:
    print(s1[0]) 
except TypeError as e:
    print(e)


print('Ix' in s1)
print('Geidi' in s1)


print(s2)
print(s3)


print(s2 | s3)
print(s2.union(s3))


print(s2 & s3)
print(s2.intersection(s3))


print(s2)
print(s3)
print(s2 - s3)
print(s2.difference(s3))


print(s2 ^ s3)
print(s2.symmetric_difference(s3))


l2 = [1, 2, 3, 4, 5]
l3 = [4, 5, 6, 7, 8]
temporary_set = set(l2).intersection(set(l3))
new_list = list(temporary_set)
print(new_list)


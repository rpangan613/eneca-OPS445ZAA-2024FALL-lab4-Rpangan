#!/usr/bin/env python3
import lab4a
import lab4b
import lab4c


set1 = {1, 2, 3, 4, 5}
set2 = {2, 1, 0, -1, -2}
print(lab4a.join_sets(set1, set2))
print(lab4a.match_sets(set1, set2))
print(lab4a.diff_sets(set1, set2))



import lab4b

list1 = [1, 2, 3, 4, 5]
list2 = [2, 1, 0, -1, -2]
print(lab4b.join_lists(list1, list2))
print(lab4b.match_lists(list1, list2))
print(lab4b.diff_lists(list1, list2))



dict_york = {
    'Address': '70 The Pond Rd',
    'City': 'Toronto',
    'Country': 'Canada',
    'Postal Code': 'M3J3M6',
    'Province': 'ON'
}
dict_newnham = {
    'Address': '1750 Finch Ave E',
    'City': 'Toronto',
    'Country': 'Canada',
    'Postal Code': 'M2J2X5',
    'Province': 'ON'
}
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

york = lab4c.create_dictionary(list_keys, list_values)
print(york)

common = lab4c.shared_values(dict_york, dict_newnham)
print(common)

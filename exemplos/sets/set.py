my_set = {1, 2, 3, 4, 5, 6}
other_set = {2, 4, 6, 8}

print(7 in my_set)

my_set.add(7)
my_set.remove(4)
print(my_set)

print(my_set.issuperset(other_set))
print(other_set.issubset(my_set))
print(my_set.isdisjoint(other_set))

print(my_set & other_set)
print(my_set | other_set)
print(my_set ^ other_set)
print(my_set - other_set)
array = [34, 56, 64, 57]
print(array)

# SLICE
print(array[1:3])
# [56, 64]

# APPEND
array.append(78)
print(array)
# [34, 56, 64, 57, 78]

# EXTEND
array2 = ["apple", "orange", "grape"]
array2.extend(array)
print(array2)
# ['apple', 'orange', 'grape', 34, 56, 64, 57, 78]

# INSERT
array.insert(0, 123)
print(array)
# [123, 34, 56, 64, 57, 78]

# REMOVE
array.remove(56)
print(array)
# [123, 34, 64, 57, 78]

# POP
array.pop(0)
print(array)
# [34, 64, 57, 78]

# INDEX
print(array.index(64))
# 1

# COUNT the number of the element given
print(array.count(64))
# 1

# SORT
array.sort()
print(array)
# [34, 57, 64, 78]

# REVERSE
array.reverse()
print(array)
# [78, 64, 57, 34]

# CLEAR
array.clear()
print(array)



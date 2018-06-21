# Trying to see if a list of lists works with the .sort() method

x = [[1], [2], [3], [4], [5]]
y = x[:]
y.append([6, 7])
y.append([1, 100, 102])
y.append([6, 8])

y.append([]) # Still works

# y.append(9) causes error
# y.append([[1]]) causes error

y.sort(reverse=True)
print(y)


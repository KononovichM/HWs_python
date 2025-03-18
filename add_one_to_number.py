def add_one(n):
    for i in range(len(n) - 1, -1, -1):
        if n[i] < 9:
            n[i] += 1
            return n
        else:
            n[i] = 0
    return [1] + n


print(add_one([9]))
print(add_one([1, 2, 3]))
print(add_one([1, 1, 9]))
print(add_one([9, 9, 9]))

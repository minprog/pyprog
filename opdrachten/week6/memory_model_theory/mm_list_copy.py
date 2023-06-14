import copy

a = [1, 2, 3]
b = copy.copy(a)
a += [100]
print(f"a: '{a}' b: '{b}'")

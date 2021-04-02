a: list[int] = [10, 20, 30]
b: list[int] = [30, 40, 50]
c: list[int] = []

i: int = 0
for i in a:
    c.append(a[i] + b[i])

print(c)

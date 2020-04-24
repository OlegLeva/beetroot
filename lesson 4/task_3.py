
l1 = [i for i in range(1,101)]
j = 0
r = 0
res = []
while j < len(l1)-1:
    if l1[j] % 7 == 0:
        res.append(l1[j])
    j += 1
while r < len(res)-1:
    if res[r] % 5 == 0:
        del res[r]
    r += 1

print(res)


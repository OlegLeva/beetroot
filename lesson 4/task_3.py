
#simplified the decision
l1 = [i for i in range(1,101)]
j = 0
res = []
while j < len(l1)-1:
    if l1[j] % 7 == 0 and l1[j] % 5:
        res.append(l1[j])
    j += 1

print(res)


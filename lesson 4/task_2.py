

import random
#l1 = set([random.randint(0,10) for r in range(10)])
#l2 = set([random.randint(0,10) for t in range(10)])
l1 = set([1,5,6,3,4,5,6,3,4,1])
l2 = set([9,8,9,7,4,4,5,6,3,3])
l3 = l1.intersection(l2)
print(list(l3))



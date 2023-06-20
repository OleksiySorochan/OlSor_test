import binarytree as bn
from binarytree import Node
# from binarytree import tree

tree = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, 13, None]

tr = bn.build(tree)
print(tr)
# print(tr.properties)
tr.pprint(index=True)
print(tr[9])
tr[9] = Node(4, left = Node(7), right = Node(8))
tr.pprint(index=True)
del tr[9]
tr.pprint()


heap = [16, 11, 9, 10, 5, 6, 8, 1, 2, 4]

hp = bn.build(heap)
# print(hp)
# print(hp.properties)
# from binarytree import *
from binarytree import tree




# root = Node(3)
# root.left = Node(5)
# root.right = Node(10)

# print(root)
# print(list(root))
# print(root.inorder)
# print(root.preorder)
# print(root.size)
# print(root.height)
# print(root.properties)
# tree = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, 13, None]

# binary_tree = build(tree)
# print(binary_tree)
# print(binary_tree.values)
# print(binary_tree.properties)

# heap = [16, 11, 9, 10, 5, 6, 8, 1, 2, 4]

# heap_tree = build(heap)
# print(heap_tree)
# print(heap_tree.values)
# print(heap_tree.properties)

root = tree()
print(root)
print(root.properties)

root2 = tree(height=2)
print(root2)

root3 = tree(height=2, is_perfect=True)
print(root3)

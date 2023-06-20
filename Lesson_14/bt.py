import random
from Tree import Node, bild

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
#
# print('Прямий обхід дерева')
# root.travers_pre_order()
# print(root.find_min())
#
# print('\nЗворотній обхід')
# root.travers_in_order()
#
# print('\nІз середини обхід')
# root.travers_enter_order()


# root = Node(28)
# root.insert(14)
# root.insert(35)
# root.insert(31)
# root.insert(10)
# root.insert(19)
# root.insert(12)
# # root.travers_pre_order()
# # root.display()
#
# b = Node(50)
# for _ in range(50):
#     b.insert(random.randint(0, 100))
#
# print(b.find_max())
# # b.display()
#
#
# c = Node(34)
# c.insert_list([12, 34, 45, 23, 12, 4, 5, 7])
# c.display()
tree = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, 13, None]

l = Node(8)
l.left = Node(3)
l.right = Node(10)
l.left.left = Node(1)
l.left.right = Node(6)
l.right.left = Node(None)
l.right.right = Node(14)
l.left.left.left = Node(None)
l.left.left.right = Node(None)
l.left.right.left = Node(4)
l.left.right.right = Node(7)
l.right.left.left = Node(None)
l.right.left.right = Node(None)
l.right.right.left = Node(13)
l.right.right.right = Node(None)

# l.display()

# a = Node(37)
# a.insert_list([10, 54, 33, 2, 54, 8, 7])
# a.find_min()
# a.find_max()
# a.display()
# a.travers_pre_order()
# print('')
# a.travers_enter_order()
# print('')
# a.travers_in_order()
# print('')
# a.travers_width()
tree = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, 13, None]
# print(tree[4])
r = bild(tree)
r.display()

r.del2(6)
# r.display()

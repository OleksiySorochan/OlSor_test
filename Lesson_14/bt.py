import random
from Tree import Node

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

l = Node(34)
l.insert_list([34, 24, 56, 78, 17, 45, 24, 78, 17])
l.display()
l.travers_in_order()
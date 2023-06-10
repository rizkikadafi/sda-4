class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root)

    def _insert_recursive(self, value, current_node: Node):
        if value <= current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(value, current_node.right)

    def display(self):
        pass

    def _display_aux(self, current_node: Node):
        if current_node.left is None and current_node.right is Node:
            len_digit = len(str(current_node.value))

            return len_digit
        elif current_node.left is None:
            data_acc = self._display_aux(current_node.right)
            return data_acc
        elif current_node.right is None:
            data_acc = self._display_aux(current_node.left)
            return data_acc
        else:
            right_data = self._display_aux(current_node.right)
            left_data = self._display_aux(current_node.left)


if __name__ == "__main__":
    bst = BST()
    data = [5, 1, 4, 3, 2]
    for d in data:
        bst.insert(d)


# class BstNode:
#     def __init__(self, key):
#         self.key = key
#         self.right = None
#         self.left = None

#     def insert(self, key):
#         if self.key == key:
#             return
#         elif self.key < key:
#             if self.right is None:
#                 self.right = BstNode(key)
#             else:
#                 self.right.insert(key)
#         else:  # self.key > key
#             if self.left is None:
#                 self.left = BstNode(key)
#             else:
#                 self.left.insert(key)

#     def display(self):
#         lines, *_ = self._display_aux()
#         for line in lines:
#             print(line)

#     def _display_aux(self):
#         """Returns list of strings, width, height, and horizontal coordinate of the root."""
#         # No child.
#         if self.right is None and self.left is None:
#             line = "%s" % self.key
#             width = len(line)
#             height = 1
#             middle = width // 2
#             return [line], width, height, middle

#         # Only left child.
#         if self.right is None:
#             lines, n, p, x = self.left._display_aux()
#             s = "%s" % self.key
#             u = len(s)
#             first_line = (x + 1) * " " + (n - x - 1) * "_" + s
#             second_line = x * " " + "/" + (n - x - 1 + u) * " "
#             shifted_lines = [line + u * " " for line in lines]
#             return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

#         # Only right child.
#         if self.left is None:
#             lines, n, p, x = self.right._display_aux()
#             s = "%s" % self.key
#             u = len(s)
#             first_line = s + x * "_" + (n - x) * " "
#             second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
#             shifted_lines = [u * " " + line for line in lines]
#             return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

#         # Two children.
#         left, n, p, x = self.left._display_aux()
#         right, m, q, y = self.right._display_aux()
#         s = "%s" % self.key
#         u = len(s)
#         first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
#         second_line = (
#             x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
#         )
#         if p < q:
#             left += [n * " "] * (q - p)
#         elif q < p:
#             right += [m * " "] * (p - q)
#         zipped_lines = zip(left, right)
#         lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
#         return lines, n + m + u, max(p, q) + 2, n + u // 2


# import random

# b = BstNode(5)
# data = [3, 1, 2, 4]
# for d in data:
#     b.insert(d)
# b.display()

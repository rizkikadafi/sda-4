from rich.table import Table

chars = {
    "up_left": "┘",
    "up_right": "└",
    "down_left": "┌",
    "down_right": "┐",
    "middle": "┴",
    "strip": "─",
}


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

    def preorder_traversal(self):
        nodes = []
        self._preorder_recursive(self.root, nodes)
        return nodes

    def _preorder_recursive(self, current_node: Node, nodes: list):
        if current_node is not None:
            nodes.append(current_node.value)
            self._preorder_recursive(current_node.left, nodes)
            self._preorder_recursive(current_node.right, nodes)

    def inorder_traversal(self):
        nodes = []
        self._inorder_recursive(self.root, nodes)
        return nodes

    def _inorder_recursive(self, current_node: Node, nodes: list):
        if current_node is not None:
            self._inorder_recursive(current_node.left, nodes)
            nodes.append(current_node.value)
            self._inorder_recursive(current_node.right, nodes)

    def postorder_traversal(self):
        nodes = []
        self._postorder_recursive(self.root, nodes)
        return nodes

    def _postorder_recursive(self, current_node: Node, nodes: list):
        if current_node is not None:
            self._postorder_recursive(current_node.left, nodes)
            self._postorder_recursive(current_node.right, nodes)
            nodes.append(current_node.value)

    def display(self):
        grid = Table.grid()

        rows, *_ = self._generate_bst_rows(self.root)
        for row in rows:
            grid.add_row(*row)
        return grid

    def _generate_bst_rows(self, current_node: Node):
        list_char_value = list(str(current_node.value))
        middle = len(list_char_value) // 2

        if (
            current_node.left is None and current_node.right is None
        ):  # Node tidak memiliki child
            row = list_char_value
            width = len(list_char_value)
            width_lr = [0, 0]
            info_child_prev = ""

            return [row], middle, width, width_lr, len(list_char_value), info_child_prev

        elif current_node.right is None:  # Node mempunyai child kiri
            (
                rows,
                middle_down,
                width,
                width_lr,
                len_char_prev,
                info_child_prev,
            ) = self._generate_bst_rows(current_node.left)

            rows = [row + [""] * len(list_char_value) for row in rows]
            first_row = [""] * width + list_char_value
            second_row = (
                [""] * (width_lr[0] + middle_down)
                + [chars["down_left"]]
                + [chars["strip"]]
                * (
                    middle_down + width_lr[1] + middle - 1
                    if len_char_prev % 2 == 0
                    else middle_down + width_lr[1] + middle
                )
                + [chars["up_left"]]
                + [""] * (middle - 1 if len(list_char_value) % 2 == 0 else middle)
            )

            if info_child_prev == "" or info_child_prev == "left":
                width_lr[0] += len_char_prev
            else:
                width_lr[0] = sum(width_lr) + len_char_prev
                width_lr[1] = 0

            info_child_prev = "left"

            return (
                [first_row, second_row] + rows,
                middle,
                width + len(list_char_value),
                width_lr,
                len(list_char_value),
                info_child_prev,
            )

        elif current_node.left is None:  # Node memiliki child kanan
            (
                rows,
                middle_down,
                width,
                width_lr,
                len_char_prev,
                info_child_prev,
            ) = self._generate_bst_rows(current_node.right)

            rows = [[""] * len(list_char_value) + row for row in rows]
            first_row = list_char_value + [""] * width
            second_row = (
                (
                    [""] * middle
                    + [chars["up_right"]]
                    + [chars["strip"]]
                    * (
                        middle + width_lr[0] + middle_down - 1
                        if len(list_char_value) % 2 == 0
                        else middle + width_lr[0] + middle_down
                    )
                )
                + [chars["down_right"]]
                + [""]
                * (
                    middle_down + width_lr[1] - 1
                    if len_char_prev % 2 == 0
                    else middle_down + width_lr[1]
                )
            )

            if info_child_prev == "" or info_child_prev == "right":
                width_lr[1] += len_char_prev
            else:
                width_lr[1] = sum(width_lr) + len_char_prev
                width_lr[0] = 0

            info_child_prev = "right"

            return (
                [first_row, second_row] + rows,
                middle,
                width + len(list_char_value),
                width_lr,
                len(list_char_value),
                info_child_prev,
            )
        else:  # Node memiliki dua child
            (
                left_rows,
                middle_down_l,
                width_l,
                width_lr_l,
                len_char_prev_l,
                _,
            ) = self._generate_bst_rows(current_node.left)

            (
                right_rows,
                middle_down_r,
                width_r,
                width_lr_r,
                len_char_prev_r,
                _,
            ) = self._generate_bst_rows(current_node.right)

            first_row = [""] * width_l + list_char_value + [""] * width_r
            second_row = (
                [""] * (width_lr_l[0] + middle_down_l)
                + [chars["down_left"]]
                + [chars["strip"]]
                * (
                    middle_down_l + width_lr_l[1] + middle - 1
                    if len_char_prev_l % 2 == 0
                    else middle_down_l + width_lr_l[1] + middle
                )
                + [chars["middle"]]
                + [chars["strip"]]
                * (
                    middle + width_lr_r[0] + middle_down_r - 1
                    if len(list_char_value) % 2 == 0
                    else middle + width_lr_r[0] + middle_down_r
                )
                + [chars["down_right"]]
                + [""]
                * (
                    middle_down_r + width_lr_r[1] - 1
                    if len_char_prev_r % 2 == 0
                    else middle_down_r + width_lr_r[1]
                )
            )

            zipped_rows = list(zip(left_rows, right_rows))
            rows = [first_row, second_row] + [
                left_row + [""] * len(list_char_value) + right_row
                for left_row, right_row in zipped_rows
            ]

            if len(left_rows) > len(right_rows):
                rows += [
                    lr + [""] * (len(list_char_value) + width_r)
                    for lr in left_rows[len(zipped_rows) :]
                ]
            elif len(right_rows) > len(left_rows):
                rows += [
                    [""] * (width_l + len(list_char_value)) + rr
                    for rr in right_rows[len(zipped_rows) :]
                ]

            width_lr = [
                sum(width_lr_l) + len_char_prev_l,
                sum(width_lr_r) + len_char_prev_r,
            ]
            info_child_prev = "middle"

            return (
                rows,
                middle,
                width_l + len(list_char_value) + width_r,
                width_lr,
                len(list_char_value),
                info_child_prev,
            )

    def delete(self, value):
        self.root = self._delete_recursive(value, self.root)

    def _delete_recursive(self, value, current_node):
        if current_node is None:
            return current_node

        if value < current_node.value:
            current_node.left = self._delete_recursive(value, current_node.left)
        elif value > current_node.value:
            current_node.right = self._delete_recursive(value, current_node.right)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            else:
                min_value = self._find_min_value(current_node.right)
                current_node.value = min_value
                current_node.right = self._delete_recursive(
                    min_value, current_node.right
                )

        return current_node

    def _find_min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value

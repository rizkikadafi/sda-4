from utils.app import *

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

    def display(self):
        grid = Table.grid()

        rows, *_ = self._display_aux(self.root)
        for row in rows:
            grid.add_row(*row)
        return grid

    def _display_aux(self, current_node: Node):
        if current_node.left is None and current_node.right is None:
            row = [str(current_node.value)]
            height = 1
            len_col_subtree = [1, 1]
            middle = len(str(current_node.value)) // 2
            return [row], height, middle, len_col_subtree

        elif current_node.left is None:
            (rows, height, middle_down, len_col_subtree) = self._display_aux(
                current_node.right
            )
            middle_up = len(str(current_node.value)) // 2
            rows = [[""] + row for row in rows]
            first_row = [str(current_node.value)]
            second_row = (
                [" " * middle_up + chars["up_right"] + chars["strip"] * middle_up]
                + [chars["strip"]] * (abs(len_col_subtree[0] - len_col_subtree[1]))
                + [(chars["strip"] * middle_down) + chars["down_right"]]
            )
            len_col_subtree[1] += 1
            return (
                [first_row, second_row] + rows,
                height + 1,
                middle_up,
                len_col_subtree,
            )
        elif current_node.right is None:
            rows, height, middle_down, len_col_subtree = self._display_aux(
                current_node.left
            )
            middle_up = len(str(current_node.value)) // 2
            first_row = [""] * (len_col_subtree[0] + len_col_subtree[1] - 1) + [
                str(current_node.value)
            ]
            second_row = (
                [" " * middle_down + chars["down_left"] + chars["strip"] * middle_down]
                + [chars["strip"]] * (len_col_subtree[1])
                + [chars["strip"] * middle_up + chars["up_left"]]
            )
            len_col_subtree[0] += 1
            return (
                [first_row, second_row] + rows,
                height + 1,
                middle_up,
                len_col_subtree,
            )
        else:
            left_rows, height_l, middle_dl, len_col_subtree_l = self._display_aux(
                current_node.left
            )
            right_rows, height_r, middle_dr, len_col_subtree_r = self._display_aux(
                current_node.left
            )

            return rows


def main():
    # data = [5, 4, 3]
    # data = [3, 444, 555]
    data = [10, 5, 7, 9, 8]
    # data = [8, 12, 10, 9]
    bst = BST()
    for d in data:
        bst.insert(d)

    console.print(bst.display(), justify="center")
    if Confirm.ask("\n[bold]Keluar Program"):
        return program4.stop()


title = "[text_title]Program 4: Title Program 4"  # untuk di tampilkan sebagai judul
name = "Program 4"  # untuk di tampilkan di list menu
description = """[text_default]
🔷 list 1. 
🔷 list 2. 
🔷 list 3.\n"""  # deskripsi program

program4 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program4.start()

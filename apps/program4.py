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
        list_char_value = list(str(current_node.value))
        middle = len(list_char_value) // 2
        info_child_prev = ""
        if current_node.left is None and current_node.right is None:
            row = list_char_value
            width = len(list_char_value)
            width_lr = [0, 0]
            return [row], middle, width, width_lr, len(list_char_value)
        elif current_node.right is None:
            rows, middle_down, width, width_lr, len_char_prev = self._display_aux(
                current_node.left
            )
            rows = [row + [""] * len(list_char_value) for row in rows]
            first_row = [""] * width + list_char_value
            second_row = (
                [""] * (width_lr[0] + (middle_down))
                + [chars["down_left"]]
                + [chars["strip"]]
                * (middle_down + width_lr[1] + middle - 1 if len_char_prev % 2 == 0 else middle_down + width_lr[1] + middle)
                + [chars["up_left"]]
                + [""] * (middle - 1 if len(list_char_value) % 2 == 0 else middle)
            )
            if info_child_prev == "" or info_child_prev == "left":     
                width_lr[0] += len_char_prev
            elif info_child_prev == "right":
                width_lr[0] = sum(width_lr) + len_char_prev
                width_lr[1] = 0
            else:
                width_lr[0] = sum(width_lr) + len_char_prev
            info_child_prev = "left"
            return (
                [first_row, second_row] + rows,
                middle,
                width + len(list_char_value),
                width_lr,
                len(list_char_value),
            )
        elif current_node.left is None:
            rows, middle_down, width, width_lr, len_char_prev = self._display_aux(
                current_node.right
            )
            rows = [[""] * len(list_char_value) + row for row in rows]
            first_row = list_char_value + [""] * width
            second_row = (
                (
                    [""] * middle
                    + [chars["up_right"]]
                    + [chars["strip"]]
                    * (
                        (middle - 1 if len(list_char_value) % 2 == 0 else middle)
                        + width_lr[0]
                        + (middle_down)
                    )
                )
                + [chars["down_right"]]
                + [""]
                * (
                    middle_down - 1 + width_lr[1]
                    if len_char_prev % 2 == 0
                    else middle_down + width_lr[1]
                )
            )
            if info_child_prev == "" or info_child_prev == "right":
                width_lr[1] += len_char_prev
            elif info_child_prev == "left":
                width_lr[1] = sum(width_lr) + len_char_prev
                width_lr[0] = 0
            else:
                width_lr[1] = sum(width_lr) + len_char_prev 
            info_child_prev = "right"
            return (
                [first_row, second_row] + rows,
                middle,
                width + len(list_char_value),
                width_lr,
                len(list_char_value),
            )
        else:
            (
                left_rows,
                middle_down_l,
                width_l,
                width_lr_l,
                len_char_prev_l,
            ) = self._display_aux(current_node.left)
            (
                right_rows,
                middle_down_r,
                width_r,
                width_lr_r,
                len_char_prev_r,
            ) = self._display_aux(current_node.right)
            first_row = [""] * width_l + list_char_value + [""] * width_r
            second_row = (
                [""] * (width_lr_l[0] + (middle_down_l))
                + [chars["down_left"]]
                + [chars["strip"]]
                * (
                    width_lr_l[1]
                    + (middle_down_l - 1 if len_char_prev_l % 2 == 0 else middle_down_l)
                    + middle
                )
                + [chars["middle"]]
                + [chars["strip"]]
                * (
                    (middle - 1 if len(list_char_value) % 2 == 0 else middle)
                    + width_lr_r[0]
                    + (middle_down_r)
                )
                + [chars["down_right"]]
                + [""] * (middle_down_r + width_lr_r[1] - 1 if len_char_prev_r % 2 == 0 else middle_down_r + width_lr_r[1])
            )
            zipped_rows = zip(left_rows, right_rows)
            rows = [first_row, second_row] + [
                lr + [""] * len(list_char_value) + rr for lr, rr in zipped_rows
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
            )

        # if current_node.left is None and current_node.right is None:
        #     list_char_value = list(str(current_node.value))
        #     rows = [list_char_value]
        #     height = 1
        #     len_col_subtree = [0, 0]
        #     middle = len(list_char_value) // 2
        #     return rows, height, middle, list_char_value, len_col_subtree

        # elif current_node.left is None:
        #     (
        #         rows,
        #         height,
        #         middle_down,
        #         list_char_prev,
        #         len_col_subtree,
        #     ) = self._display_aux(current_node.right)
        #     list_char_value = list(str(current_node.value))
        #     middle_up = len(list_char_value) // 2
        #     rows = [[""] * len(list_char_value) + row for row in rows]
        #     first_row = list_char_value
        #     second_row = (
        #         [""] * middle_up
        #         + [chars["up_right"]]
        #         + [chars["strip"]]
        #         * (middle_up - 1 if len(list_char_value) % 2 == 0 else middle_up)
        #         + [chars["strip"]] * (middle_down)
        #         + [chars["down_right"]]
        #     )
        #     len_col_subtree[1] += 1 + len_col_subtree[0]
        #     return (
        #         [first_row, second_row] + rows,
        #         height + 1,
        #         middle_up,
        #         list_char_value,
        #         len_col_subtree,
        #     )
        # elif current_node.right is None:
        #     (
        #         rows,
        #         height,
        #         middle_down,
        #         list_char_prev,
        #         len_col_subtree,
        #     ) = self._display_aux(current_node.left)
        #     list_char_value = list(str(current_node.value))
        #     middle_up = len(list_char_value) // 2
        #     first_row = [""] * len(list_char_prev) + list_char_value
        #     second_row = (
        #         [""] * (middle_down)
        #         + [chars["down_left"]]
        #         + [chars["strip"]]
        #         * (middle_down - 1 if len(list_char_prev) % 2 == 0 else middle_down)
        #         + [chars["strip"]] * (middle_up)
        #         + [chars["up_left"]]
        #     )
        #     len_col_subtree[0] += 1 + len_col_subtree[1]
        #     return (
        #         [first_row, second_row] + rows,
        #         height + 1,
        #         middle_up,
        #         list_char_value,
        #         len_col_subtree,
        #     )
        # else:
        #     left_rows, height_l, middle_dl, len_col_subtree_l = self._display_aux(
        #         current_node.left
        #     )
        #     right_rows, height_r, middle_dr, len_col_subtree_r = self._display_aux(
        #         current_node.left
        #     )

        #     return rows


def main():
    # data = [200, 150, 140]
    # data = [200, 300, 150, 250, 160, 240, 170]
    # data = [200, 150, 140, 130, 280, 270, 260, 275]
    data = [200, 280, 270, 260, 275]
    # data = [200, 300, 450]
    data = input("masukkan data: ").split()
    data = [int(d) for d in data]
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

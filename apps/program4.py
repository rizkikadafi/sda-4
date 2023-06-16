from utils.app import *

from data_structure.bst import BST


def main():
    data = input("masukkan data: ").split()
    data = [int(d) for d in data]
    bst = BST()
    for d in data:
        bst.insert(d)

    console.print(bst.display(), justify="center")
    console.print("Preorder", bst.preorder_traversal())
    console.print("Inorder", bst.inorder_traversal())
    console.print("Postorder", bst.postorder_traversal())
    if Confirm.ask("\n[bold]Keluar Program"):
        return program4.stop()


title = "[text_title]Program 4: Binary Search Tree"  # untuk di tampilkan sebagai judul
name = "Binary Search Tree"  # untuk di tampilkan di list menu
description = """[text_default]
🔷 list 1. 
🔷 list 2. 
🔷 list 3.\n"""  # deskripsi program

program4 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program4.start()

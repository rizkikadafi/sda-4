from utils.app import *


def main():
    if Confirm.ask("\n[bold]Keluar Program"):
        return program3.stop()


title = "[text_title]Program 3: Title Program 3"  # untuk di tampilkan sebagai judul
name = "Program 3"  # untuk di tampilkan di list menu
description = """[text_default]
🔷 list 1. 
🔷 list 2. 
🔷 list 3.\n"""  # deskripsi program

program3 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program3.start()

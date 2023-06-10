from utils.app import *

chars = ["┘", "┌", "─", "└", "┐", "┴"]


def main():
    grid = Table.grid(padding=(0, 0))

    x = [Align(str(i), align="center") for i in range(1, 21)]
    grid.add_row("", Align("20", align="center"), "")
    grid.add_row(
        Align(" ┌─", align="center"),
        Align("─" * 5 + "┴" + "─" * 5, align="center"),
        "┐",
    )
    grid.add_row(Align("5", align="center"), "", Align("25", align="center"))
    grid.add_row(
        Align("", align="center"),
        Align("─" * 2, align="right"),
        Align("┘", align="center"),
    )

    console.print(grid, justify="center")
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

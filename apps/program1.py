from utils.app import *


def bubble_sort(data):
    for i in range(1, len(data)):
        table_process = Table(title=f"Tahap {i}")
        table_process.add_column("Data")
        table_process.add_column("Swap")

        list_data_str = [str(d) for d in data]
        for j in range(len(data) - i):
            swap = False
            current = list_data_str.copy()
            current[j] = f"[bold blue]{current[j]}[/]"
            current[j + 1] = f"[bold blue]{current[j+1]}[/]"
            if data[j] > data[j + 1]:
                swap = True
                current[j], current[j + 1] = current[j + 1], current[j]
            table_process.add_row(f"{' '.join(current)}", str(swap))

        console.print(table_process)


def main():
    data = [25, 57, 48, 39, 18, 95, 80, 35]
    bubble_sort(data)
    if Confirm.ask("\n[bold]Keluar Program"):
        return program1.stop()


title = "[text_title]Program 1: Buble Sort"  # untuk di tampilkan sebagai judul
name = "Buble Sort"  # untuk di tampilkan di list menu
description = """[text_default]
🔷 Program 1 merupakan program untuk mengurutkan data dengan menggunakan algoritma Buble Sort. 
🔷 Data yang diurutkan bisa berupa angka ataupun alphabet.\n"""  # deskripsi program

program1 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program1.start()

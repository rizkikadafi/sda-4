from utils.app import *


class NumericPrompt(PromptBase):
    response_type = str
    validate_error_massage = "[prompt.invalid]Harap masukkan data numerik \[bilangan bulat atau pecahan]! (contoh: 2 atau 3.2)"

    def process_response(self, value: str):
        list_value = value.split()
        for d in list_value:
            if not str(d).replace(".", "").isnumeric():
                raise InvalidResponse(self.validate_error_massage)

        return value


def selection_sort(data: list):
    list_data = data.copy()
    list_data_str = [f"[text_default]{str(d)}[/]" for d in list_data]

    grid_process = Table.grid(expand=True)

    list_row = []
    for i in range(len(data) - 1):
        i_min = i
        table_process = Table(title=f"Tahap ke-{i + 1}", min_width=30)
        table_process.add_column("Data")
        table_process.add_column("Ket")

        list_data_str[i_min] = list_data_str[i_min].replace(
            "text_default", "bold yellow"
        )

        table_process.add_row(
            f"{' '.join(list_data_str)}", f"min = {list_data[i_min]} (awal)"
        )

        for j in range(i + 1, len(data)):
            list_data_str[j - 1] = list_data_str[j - 1].replace(
                "bold blue", "text_default"
            )

            list_data_str[j] = list_data_str[j].replace("text_default", "bold blue")

            if list_data[j] < list_data[i_min]:
                list_data_str[i_min] = list_data_str[i_min].replace(
                    "bold yellow", "text_default"
                )

                i_min = j

                list_data_str[i_min] = list_data_str[i_min].replace(
                    "bold blue", "bold yellow"
                )

            table_process.add_row(
                f"{' '.join(list_data_str)}", f"min = {list_data[i_min]}"
            )

        list_data_str[len(data) - 1] = list_data_str[len(data) - 1].replace(
            "bold blue", "text_default"
        )

        if i_min != i:
            list_data[i], list_data[i_min] = list_data[i_min], list_data[i]
            list_data_str[i_min] = list_data_str[i_min].replace(
                "bold yellow", "bold green"
            )

            list_data_str[i], list_data_str[i_min] = (
                list_data_str[i_min],
                list_data_str[i],
            )

            table_process.add_row(f"{' '.join(list_data_str)}", "Swap (akhir)")
        else:
            list_data_str[i_min] = list_data_str[i_min].replace(
                "bold yellow", "bold green"
            )

            table_process.add_row(f"{' '.join(list_data_str)}", "(akhir)")

        list_row.append(Align(table_process, align="center"))
        if (i + 1) % 2 == 0 or i == len(data) - 1:
            grid_process.add_row(*list_row)
            list_row = []

    console.print(grid_process)
    return list_data


def main():
    x = [3, 4, 5, 2, 1]
    print(x)
    print(selection_sort(x))
    if Confirm.ask("\n[bold]Keluar Program"):
        return program3.stop()


title = "[text_title]Program 3: Selection Sort"  # untuk di tampilkan sebagai judul
name = "Selection Sort"  # untuk di tampilkan di list menu
description = """[text_default]
🔷 Program 3 merupakan program untuk mengurutkan data dengan menggunakan algoritma Selection Sort. 
🔷 Data yang diurutkan bisa berupa angka ataupun alphabet.\n"""  # deskripsi program

program3 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program3.start()

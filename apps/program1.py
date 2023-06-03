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


def bubble_sort(data: list):
    list_data = data.copy()

    grid_process = Table.grid(expand=True)

    list_row = []
    for i in range(1, len(data)):
        table_process = Table(
            title=f"Tahap {i}",
        )
        table_process.add_column(Align("Data", align="center"), min_width=15)
        table_process.add_column("Swap", min_width=5, justify="center")

        list_data_str = [str(d) for d in list_data]
        list_data_str[0] = f"[bold blue]{list_data_str[0]}[/]"

        for j in range(len(data) - i):
            if j > 0:
                list_data_str[j - 1] = list_data_str[j - 1].replace(
                    "bold blue", "text_default"
                )
                list_data_str[j - 1] = list_data_str[j - 1].replace(
                    "bold green", "text_default"
                )

            swap = False
            list_data_str[j + 1] = f"[bold blue]{list_data_str[j+1]}[/]"

            if list_data[j] > list_data[j + 1]:
                list_data[j], list_data[j + 1] = list_data[j + 1], list_data[j]

                swap = True
                list_data_str[j], list_data_str[j + 1] = (
                    list_data_str[j + 1],
                    list_data_str[j],
                )

                list_data_str[j] = list_data_str[j].replace("bold blue", "bold green")
                list_data_str[j + 1] = list_data_str[j + 1].replace(
                    "bold blue", "bold green"
                )
            else:
                list_data_str[j] = list_data_str[j].replace("bold green", "bold blue")

            table_process.add_row(f"{' '.join(list_data_str)}", str(swap))

        list_row.append(Align(table_process, align="center"))
        if i % (2 if len(data) > 12 else 3) == 0 or i == len(data) - 1:
            grid_process.add_row(*list_row)
            list_row = []

    return ([str(d) for d in list_data], grid_process)


def main():
    data_type = {
        1: "Numerik",
        2: "String",
    }

    data_type_str = "\n[text_default]"
    for k, v in data_type.items():
        data_type_str += f"{k}. {v}\n"

    panel_data_type = Panel(
        data_type_str,
        title="[text_title]Tipe Data",
        title_align="left",
        style="default",
    )

    console.print(Padding(panel_data_type, pad=(1, 0, 0, 0)))
    dt = IntPrompt.ask(
        "\n[bold]Pilih Tipe Data", choices=[str(i) for i in data_type.keys()]
    )

    list_data = []
    match dt:
        case 1:
            data = NumericPrompt.ask(
                "\n[bold]Masukkan data Numerik (dipisahkan dengan spasi)"
            )
            list_data = [
                int(d) if str(d).find(".") == -1 else float(d) for d in data.split()
            ]
        case 2:
            data = Prompt.ask("\n[bold]Masukkan data String (dipisahkan dengan spasi)")
            list_data = data.split()

    grid_result = Table.grid(expand=True)
    grid_result.add_column(ratio=3, vertical="middle")
    grid_result.add_column(ratio=1, vertical="middle")
    grid_result.add_column(ratio=3, vertical="middle")

    sorted_data = bubble_sort(list_data)

    original_data_str = [str(d) for d in list_data]
    panel_orginal_data = Panel(
        Text(
            f"\n{' '.join(original_data_str)}\n", justify="center", style="text_default"
        ),
        title="[text_title]Original Data",
        title_align="center",
        style="default",
    )
    panel_sorted_data = Panel(
        Text(f"\n{' '.join(sorted_data[0])}\n", justify="center", style="text_default"),
        title="[text_title]Sorted Data",
        title_align="center",
        style="default",
    )

    grid_result.add_row(
        panel_orginal_data,
        Text(" ---> ", justify="center", style="text_default"),
        panel_sorted_data,
    )

    if Confirm.ask("\n[bold]Apakah anda ingin menampilkan proses sorting"):
        console.clear()
        console.rule(program1.title, style="default")
        console.print(Padding(grid_result, pad=(1, 0)))
        console.print(Padding(sorted_data[1], pad=(0, 0, 1, 0)))
    else:
        console.clear()
        console.rule(program1.title, style="default")
        console.print(Padding(grid_result, pad=(1, 0)))

    if Confirm.ask("[bold]Keluar Program"):
        return program1.stop()


title = "[text_title]Program 1: Bubble Sort"  # untuk di tampilkan sebagai judul
name = "Bubble Sort"  # untuk di tampilkan di list menu
description = """[text_default]
🔷 Program 1 merupakan program untuk mengurutkan data dengan menggunakan algoritma Buble Sort. 
🔷 Data yang diurutkan bisa berupa angka ataupun alphabet.\n"""  # deskripsi program

program1 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program1.start()

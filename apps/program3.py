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

            if i + 1 == len(data) - 1:
                list_data_str[len(data) - 1] = list_data_str[len(data) - 1].replace(
                    "text_default", "bold green"
                )

            table_process.add_row(f"{' '.join(list_data_str)}", "Swap (akhir)")
        else:
            list_data_str[i_min] = list_data_str[i_min].replace(
                "bold yellow", "bold green"
            )
            if i + 1 == len(data) - 1:
                list_data_str[len(data) - 1] = list_data_str[len(data) - 1].replace(
                    "text_default", "bold green"
                )

            table_process.add_row(f"{' '.join(list_data_str)}", "(akhir)")

        list_row.append(Align(table_process, align="center"))
        if (i + 1) % 2 == 0 or i == len(data) - 1:
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

    sorted_data = selection_sort(list_data)

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
        console.rule(program3.title, style="default")
        console.print(Padding(grid_result, pad=(1, 0)))
        console.print(Padding(sorted_data[1], pad=(0, 0, 1, 0)))
    else:
        console.clear()
        console.rule(program3.title, style="default")
        console.print(Padding(grid_result, pad=(1, 0)))

    if Confirm.ask("[bold]Keluar Program"):
        return program3.stop()


title = "[text_title]Program 3: Selection Sort"  # untuk di tampilkan sebagai judul
name = "Selection Sort"  # untuk di tampilkan di list menu
description = """[text_default]
🔷 Program 3 merupakan program untuk mengurutkan data dengan menggunakan algoritma Selection Sort. 
🔷 Data yang diurutkan bisa berupa angka ataupun alphabet.\n"""  # deskripsi program

program3 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program3.start()

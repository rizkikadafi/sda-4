from utils.app import *

box = "⬜"


class NumericPrompt(PromptBase):
    response_type = str
    validate_error_massage = "[prompt.invalid]Harap masukkan data numerik \[bilangan bulat atau pecahan]! (contoh: 2 atau 3.2)"

    def process_response(self, value: str):
        list_value = value.split()
        for d in list_value:
            if not str(d).replace(".", "").isnumeric():
                raise InvalidResponse(self.validate_error_massage)

        return value


def insertion_sort(data: list):
    list_data = data.copy()
    for i in range(1, len(data)):
        tmp = list_data[i]

        j = i
        while j > 0 and list_data[j - 1] > tmp:
            list_data[j] = list_data[j - 1]
            j -= 1
        list_data[j] = tmp
    return [str(d) for d in list_data]


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

    sorted_data = insertion_sort(list_data)

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
        Text(f"\n{' '.join(sorted_data)}\n", justify="center", style="text_default"),
        title="[text_title]Sorted Data",
        title_align="center",
        style="default",
    )

    grid_result.add_row(
        panel_orginal_data,
        Text(" ---> ", justify="center", style="text_default"),
        panel_sorted_data,
    )

    console.clear()
    console.rule(program2.title, style="default")
    console.print(Padding(grid_result, pad=(1, 0)))

    if Confirm.ask("\n[bold]Keluar Program"):
        return program2.stop()


title = "[text_title]Program 2: Insertion Sort"  # untuk di tampilkan sebagai judul
name = "Insertion Sort"  # untuk di tampilkan di list menu
description = """[text_default]
🔷 Program 2 merupakan program untuk mengurutkan data dengan menggunakan algoritma Buble Sort. 
🔷 Data yang diurutkan bisa berupa angka ataupun alphabet.\n"""  # deskripsi program

program2 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program2.start()

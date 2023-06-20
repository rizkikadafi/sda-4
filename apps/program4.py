from utils.app import *

from data_structure.bst import BST


def success_panel(operation: str, data1=None, data2=None) -> Panel:
    """Panel untuk menampilkan info ketika operasi tertentu berhasil dilakukan."""

    panel = Panel("None")
    match operation:
        case "addition":
            panel = Panel(
                Text(
                    f"\nData {data1} berhasil dimasukkan ke dalam BST.\n",
                    justify="center",
                    style="text_success",
                ),
                title="[title_success]INFO",
                style="success",
            )
        case "deletion":
            if data2:
                panel = Panel(
                    Text(
                        f"\nData {data2} tidak ada dalam BST!\nData {data1} telah dihapus dari BST.\n",
                        justify="center",
                        style="text_success",
                    ),
                    title="[title_success]INFO",
                    style="success",
                )
            else:
                panel = Panel(
                    Text(
                        f"\nData {data1} telah dihapus dari BST.\n",
                        justify="center",
                        style="text_success",
                    ),
                    title="[title_success]INFO",
                    style="success",
                )
        case "reset":
            panel = Panel(
                Text(
                    f"\nSeluruh data dalam BST telah dihapus!.\n",
                    justify="center",
                    style="text_success",
                ),
                title="[title_success]INFO",
                style="success",
            )
    return panel


def empty_data_panel(operation: str) -> Panel:
    """Panel untuk menampilkan info ketika data kosong."""

    panel = Panel("None")
    match operation:
        case "deletion":
            panel = Panel(
                Text(
                    "\nBST Kosong! Tidak ada data yang bisa dihapus!\n",
                    justify="center",
                    style="text_warning",
                ),
                title="[title_warning]INFO",
                style="warning",
            )
        case "display_data":
            panel = Panel(
                Text(
                    "\nBST Kosong! Tidak ada data yang bisa ditampilkan!\n",
                    justify="center",
                    style="text_warning",
                ),
                title="[title_warning]INFO",
                style="warning",
            )

    return panel


class ListNumericPrompt(PromptBase):
    response_type = str
    validate_error_message = "[prompt.invalid]Harap masukkan data numerik!"

    def process_response(self, value: str):
        list_value = value.split()
        list_value_int = []
        for d in list_value:
            if not d.isnumeric():
                raise InvalidResponse(self.validate_error_message)
            else:
                list_value_int.append(int(d))

        return list_value_int


class ListStringPrompt(PromptBase):
    response_type = str
    validate_error_message = "[prompt.invalid]Harap masukkan data numerik!"

    def process_response(self, value: str):
        list_value = value.split()

        return list_value


def main():
    data_type = {1: "Numerik", 2: "String"}

    data_type_str = "\n[text_default]"
    for k, v in data_type.items():
        data_type_str += f"{k}. {v}\n"

    panel_data_type = Panel(
        data_type_str,
        title="[text_title]Tipe Data",
        title_align="left",
        style="default",
    )

    menu = {
        1: "Insert Data",
        2: "Display Data",
        3: "Traverse Data",
        4: "Remove Data",
        5: "Reset Data",
        6: "Change Data Type",
        7: "Keluar Program",
    }
    menu_str = "\n[text_default]"
    for k, v in menu.items():
        menu_str += f"{k}. {v}\n"

    panel_menu = Panel(
        menu_str,
        title="[text_title]Menu Program",
        title_align="left",
        style="default",
    )

    console.print(Padding(panel_data_type, pad=(1, 0, 0, 0)))
    dt = IntPrompt.ask(
        "\n[bold]Pilih Tipe Data", choices=[str(i) for i in data_type.keys()]
    )

    bst = BST()
    list_data_all = []
    import getpass

    while True:
        console.clear()
        console.rule(program4.title, style="default")
        console.print(Padding(panel_menu, pad=(1, 0, 0, 0)))

        menu_opt = IntPrompt.ask(
            "\n[bold]Pilih Menu", choices=[str(i) for i in menu.keys()]
        )
        list_data = []
        match menu_opt:
            case 1:
                if data_type[dt] == "Numerik":
                    list_data = ListNumericPrompt.ask(
                        "\n[bold]Masukkan data (pisahkan dengan spasi jika lebih dari satu)"
                    )
                    list_data_all += list_data
                else:
                    list_data = ListStringPrompt.ask(
                        "\n[bold]Masukkan data (pisahkan dengan spasi jika lebih dari satu)"
                    )
                    list_data_all += list_data

                for data in list_data:
                    bst.insert(data)
                console.print(success_panel(data1=list_data, operation="addition"))
                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")

            case 2:
                if bst.empty():
                    console.print(empty_data_panel(operation="display_data"))
                else:
                    console.clear()
                    console.rule(program4.title, style="default")
                    console.print(
                        Panel(
                            Align(
                                f"\n{str(list_data_all)}\n",
                                align="center",
                                style="text_default",
                            ),
                            title="[text_title]List Data",
                            title_align="center",
                            style="default",
                        )
                    )
                    console.print(
                        Panel(
                            Align(
                                Group("", bst.display(), ""),
                                align="center",
                                style="text_default",
                            ),
                            title="[text_title]BST Structure",
                            title_align="center",
                            style="default",
                        )
                    )
                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 3:
                if bst.empty():
                    console.print(empty_data_panel(operation="display_data"))
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    continue

                panel_bst = Padding(
                    Panel(
                        Align(
                            Group("", bst.display(), ""),
                            align="center",
                            style="text_default",
                        ),
                        title="[text_title]BST Structure",
                        title_align="center",
                        style="default",
                    ),
                    pad=(1, 0, 0, 0),
                )
                panel_preorder = Padding(
                    Panel(
                        Align(
                            "\n" + str(bst.preorder_traversal()) + "\n",
                            align="center",
                            style="text_default",
                        ),
                        style="default",
                        title="[text_title]Preorder Traversal",
                        title_align="center",
                    ),
                    pad=(1, 0, 0, 0),
                )
                panel_inorder = Padding(
                    Panel(
                        Align(
                            "\n" + str(bst.inorder_traversal()) + "\n",
                            align="center",
                            style="text_default",
                        ),
                        style="default",
                        title="[text_title]Inorder Traversal",
                        title_align="center",
                    ),
                    pad=(1, 0, 0, 0),
                )
                panel_postorder = Padding(
                    Panel(
                        Align(
                            "\n" + str(bst.postorder_traversal()) + "\n",
                            align="center",
                            style="text_default",
                        ),
                        style="default",
                        title="[text_title]Postorder Traversal",
                        title_align="center",
                    ),
                    pad=(1, 0, 0, 0),
                )
                console.clear()
                console.rule(program4.title, style="default")
                console.print(
                    Group(panel_bst, panel_preorder, panel_inorder, panel_postorder)
                )
                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 4:
                if bst.empty():
                    console.print(empty_data_panel(operation="deletion"))
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    continue

                if data_type[dt] == "Numerik":
                    remove_list_data = ListNumericPrompt.ask(
                        "\n[bold]Masukkan data yang ingin dihapus (pisahkan dengan spasi jika lebih dari satu)"
                    )
                else:
                    remove_list_data = ListStringPrompt.ask(
                        "\n[bold]Masukkan data yang ingin dihapus (pisahkan dengan spasi jika lebih dari satu)"
                    )

                if Confirm.ask(
                    "\n[bold]Apakah anda yakin ingin menghapus data tersebut?"
                ):
                    not_in_bst = []
                    in_bst = []
                    for data in remove_list_data:
                        if data not in list_data_all:
                            not_in_bst.append(data)
                            continue
                        in_bst.append(data)
                        bst.delete(data)
                        list_data_all.remove(data)
                    console.print(
                        success_panel(
                            data1=in_bst, data2=not_in_bst, operation="deletion"
                        )
                    )
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 5:
                if bst.empty():
                    console.print(empty_data_panel(operation="deletion"))
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    continue

                if Confirm.ask(
                    "\n[bold]Apakah anda yakin ingin menghapus seluruh data dalam BST?"
                ):
                    bst.reset()
                    list_data_all.clear()
                    console.print(success_panel(operation="reset"))
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 6:
                if not bst.empty():
                    console.print(
                        "[prompt.invalid]Untuk mengubah tipe data, BST harus dikosongkan! Harap reset terlebih dahulu."
                    )
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                else:
                    break
            case 7:
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

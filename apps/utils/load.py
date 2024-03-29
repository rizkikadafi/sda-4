from .app import App, Panel, Padding, IntPrompt, Confirm, Text, console


class Load(App):
    def add(self, programs):
        self.programs = programs

    def start(self):
        menus = "\n[text_default]"
        for i in range(len(self.programs) + 1):
            if i == len(self.programs):
                menus += f"{i+1}. Keluar Program\n"
            else:
                menus += f"{i+1}. {self.programs[i].name}\n"

        panel_menu = Panel(menus, title="[text_title]Menu Program", title_align="left")
        panel_description = Panel(
            self.description, title="[text_title]Deskripsi", title_align="left"
        )
        panel_closing = Panel(
            Text(
                "\n🙏Terima kasih telah menggunakan aplikasi ini🙏\n",
                justify="center",
                style="text_default",
            ),
            title="[text_title]Program Selesai",
            style="default",
        )

        while True:
            console.clear()
            console.rule(self.title, style="default")
            console.print(Padding(panel_description, pad=(1, 0, 0, 0)), style="default")
            console.print(Padding(panel_menu, pad=(1, 0, 0, 0)), style="default")

            opt = IntPrompt.ask(
                "[bold]\nPilih Menu",
                choices=[str(i + 1) for i in range(len(self.programs) + 1)],
            )
            if opt == len(self.programs) + 1:
                console.clear()
                console.print(panel_closing)

                break
            else:
                self.programs[opt - 1].start()

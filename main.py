import sys

sys.path.append("apps")

from apps.utils.load import Load
from apps import program1, program2, program3, program4

title = "[text_title]Project SDA 4[/]"
description = """[text_default]
Project SDA 4 merupakan project mata kuliah Struktur Data dan Algoritma yang berisi program-program untuk pengurutan data.
"""

programs = Load(title=title, description=description)
programs.add([program1, program2, program3, program4])

if __name__ == "__main__":
    programs.start()

from abstract import AbstractCheckbox


class WinCheckbox(AbstractCheckbox):
    """Чекбокс для ОС Windows."""

    def click_checkbox(self):
        print("Вы выбрали чекбокс windows!")


class MacCheckbox(AbstractCheckbox):
    """Чекбокс для ОС Mac."""

    def click_checkbox(self):
        print("Вы выбрали чекбокс mac!")


class GnomeCheckbox(AbstractCheckbox):
    """Чекбокс для ОС UNIX."""

    def click_checkbox(self):
        print("Вы выбрали чекбокс gnome!")

from abstract import AbstractRadioButton


class WinRadioButton(AbstractRadioButton):
    """Radiobutton для ОС Windows."""

    def click_radiobutton(self):
        print("Вы выбрали radiobutton windows!")


class MacRadioButton(AbstractRadioButton):
    """Radiobutton для ОС Mac."""

    def click_radiobutton(self):
        print("Вы выбрали radiobutton mac!")


class GnomeRadioButton(AbstractRadioButton):
    """Radiobutton для ОС UNIX."""

    def click_radiobutton(self):
        print("Вы выбрали radiobutton gnome!")

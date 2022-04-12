from abstract import AbstractButton


class WinButton(AbstractButton):
    """Кнопка для ОС Windows."""

    def click_button(self):
        print("Вы нажали на кнопку windows!")


class MacButton(AbstractButton):
    """Кнопка для ОС Mac."""

    def click_button(self):
        print("Вы нажали на кнопку mac!")


class GnomeButton(AbstractButton):
    """Кнопка для ОС Unix."""

    def click_button(self):
        print("Вы нажали на кнопку gnome!")

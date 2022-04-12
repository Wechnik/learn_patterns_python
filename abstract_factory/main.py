from contextlib import suppress

from abstract import GUIElements
from abstract_factory import FactoryGUI, SystemEnum


class Application:
    """Приложение, которео использует GUI."""

    def __init__(self, GUI: GUIElements):
        self._gui = GUI

    def click_button(self) -> None:
        """Обрабатывает нажатие на кнопку."""
        self._gui.button.click_button()

    def click_checkbox(self) -> None:
        """Обрабатывает нажатие на кнопку."""
        self._gui.checkbox.click_checkbox()

    def click_radiobutton(self) -> None:
        """Обрабатывает нажатие на кнопку."""
        self._gui.radiobutton.click_radiobutton()


if __name__ == '__main__':

    # Пример работы на WIN
    GUI: GUIElements = FactoryGUI.get_gui(SystemEnum.WIN)
    app = Application(GUI)

    app.click_button()
    app.click_checkbox()
    app.click_radiobutton()

    # Пример работы на Mac
    GUI: GUIElements = FactoryGUI.get_gui(SystemEnum.MAC)
    app = Application(GUI)

    app.click_button()
    app.click_checkbox()
    app.click_radiobutton()

    # Пример работы на Gnome
    GUI: GUIElements = FactoryGUI.get_gui(SystemEnum.GNOME)
    app = Application(GUI)

    app.click_button()
    app.click_checkbox()
    app.click_radiobutton()

    # Пример работы с ошибкой
    with suppress(KeyError):
        GUI: GUIElements = FactoryGUI.get_gui(SystemEnum.OTHER)
        app = Application(GUI)
        app.click_button()

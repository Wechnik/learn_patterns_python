from enum import Enum, auto
from typing import Optional

from GUI.button import WinButton, MacButton, GnomeButton
from GUI.checkbox import WinCheckbox, MacCheckbox, GnomeCheckbox
from GUI.radiobutton import WinRadioButton, MacRadioButton, GnomeRadioButton
from abstract import AbstractFactoryGUI, GUIElements


class WinFactory(AbstractFactoryGUI):
    """Фабрика пораждающая элементы графического интерфейса Windows."""

    @staticmethod
    def create_gui_elements() -> GUIElements:
        """Возвращает элементы графического интерфейса."""
        return GUIElements(
            button=WinButton(),
            checkbox=WinCheckbox(),
            radiobutton=WinRadioButton(),
        )


class MacFactory(AbstractFactoryGUI):
    """Фабрика пораждающая элементы графического интерфейса Mac."""

    @staticmethod
    def create_gui_elements() -> GUIElements:
        """Возвращает элементы графического интерфейса."""
        return GUIElements(
            button=MacButton(),
            checkbox=MacCheckbox(),
            radiobutton=MacRadioButton(),
        )


class GnomeFactory(AbstractFactoryGUI):
    """Фабрика пораждающая элементы графического интерфейса Gnome."""

    @staticmethod
    def create_gui_elements() -> GUIElements:
        """Возвращает элементы графического интерфейса."""
        return GUIElements(
            button=GnomeButton(),
            checkbox=GnomeCheckbox(),
            radiobutton=GnomeRadioButton(),
        )


class SystemEnum(Enum):
    """Енум допустимых операционных систем."""

    WIN = auto()
    MAC = auto()
    GNOME = auto()
    OTHER = auto()


class FactoryGUI:

    @staticmethod
    def get_gui(system_name: SystemEnum) -> Optional[GUIElements]:
        """Возвращает GUI."""
        if system_name == SystemEnum.WIN:
            return WinFactory.create_gui_elements()
        elif system_name == SystemEnum.MAC:
            return MacFactory.create_gui_elements()
        elif system_name == SystemEnum.GNOME:
            return GnomeFactory.create_gui_elements()
        print('Выбрана недопустимая ОС!')
        raise KeyError("Данная программа не может быть запущена на Вашей системе!")

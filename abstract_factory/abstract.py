from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


class AbstractButton(metaclass=ABCMeta):
    """Абстрактный класс кнопки."""

    @abstractmethod
    def click_button(self):
        """Обработывает событие клика на кнопку."""
        raise NotImplementedError


class AbstractCheckbox(metaclass=ABCMeta):
    """Абстрактный класс чек-бокса."""

    @abstractmethod
    def click_checkbox(self):
        """Обработывает событие клика на чек-бокс."""
        raise NotImplementedError


class AbstractRadioButton(metaclass=ABCMeta):
    """Абстрактный класс radiobutton."""

    @abstractmethod
    def click_radiobutton(self):
        """Обработывает событие клика на radiobutton."""
        raise NotImplementedError


@dataclass
class GUIElements:
    """Датакласс элементов GUI."""

    button: AbstractButton
    checkbox: AbstractCheckbox
    radiobutton: AbstractRadioButton


class AbstractFactoryGUI(metaclass=ABCMeta):
    """Абстрактная фабрика пораждающая элементы графического интерфейса."""

    @staticmethod
    @abstractmethod
    def create_gui_elements() -> GUIElements:
        """Создаёт элементы под определённую ОС."""
        raise NotImplementedError

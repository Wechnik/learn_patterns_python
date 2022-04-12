from abc import abstractmethod, ABCMeta


class AbstractShop(metaclass=ABCMeta):
    """Интерфейс объектов магазина."""

    @abstractmethod
    def get_information(self) -> str:
        """Возвращает информацию о магазине."""
        raise NotImplementedError


class AbstractCreaterShop(metaclass=ABCMeta):
    """Фабрика для создания и работы с магазинами."""

    @abstractmethod
    def get_shop(self) -> AbstractShop:
        """Возвращает объект магазина."""
        raise NotImplementedError

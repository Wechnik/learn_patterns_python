from typing import Optional

from factory_method.abstract import AbstractCreaterShop, AbstractShop


class AutoShop(AbstractShop):
    """Магазин автозапчастей."""

    def get_information(self) -> str:
        """Возвращает информацию о магазине."""
        return "В данном автомагазине есть все необходимые запчасти для содержания Вашего авто!"


class DressShop(AbstractShop):
    """Магазин одежды."""

    def get_information(self) -> str:
        """Возвращает информацию о магазине."""
        return "Лучшая верхняя одежда в городе!"


class CreatorShop(AbstractCreaterShop):
    """Создаёт магазины автозапчастей."""

    def get_shop(self, name: str) -> Optional[AbstractShop]:
        name = name.lower()
        if 'auto' in name:
            return AutoShop()
        if 'dress' in name:
            return DressShop()



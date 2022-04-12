from factory_method.abstract import AbstractShop
from factory_method.factory_method import CreatorShop


def work_processes(shop: AbstractShop):
    """Клиентский код."""
    print(shop.get_information())


if __name__ == '__main__':
    work_processes(CreatorShop().get_shop('AutoPart'))
    work_processes(CreatorShop().get_shop('AutoShop'))
    work_processes(CreatorShop().get_shop('12dress'))

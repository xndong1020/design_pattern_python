from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    """
    Abstract class for concrete products(drinks)
    """

    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("This is a tea product")


class Coffee(HotDrink):
    def consume(self):
        print("This is a Coffee product")


class HotDrinkFactory(ABC):
    """
    Abstract class for a family of factories
    """

    def produce(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def produce(self, amount=2):
        print(f"{amount} {'cups' if amount > 1 else 'cup'} of Tea has been produced")
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def produce(self, amount=2):
        print(f"{amount} {'cups' if amount > 1 else 'cup'} of Coffee has been produced")
        return Coffee()


class Drinks(Enum):
    TEA = auto()
    COFFEE = auto()


if __name__ == "__main__":
    target_product = "COFFEE"

    if target_product not in Drinks.__members__:
        raise ValueError(f"{target_product} is not supported product type.")

    # capitalize first letter, lower remaining letters
    # eg: 'COFFEE' to 'Coffee'
    product_name = f"{target_product[0]}{target_product[1:].lower()}"

    factory_name = f"{product_name}Factory"

    factory_instance = eval(factory_name)()

    product = factory_instance.produce()

    print("product produced:", type(product))

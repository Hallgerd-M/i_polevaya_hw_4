class Product:
    """Продукт"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product: dict):
        """Взвращает созданный объект класса Product из параметров товара в словаре"""
        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def get_price(self):
        return self.__price

    @get_price.setter
    def get_price(self):
        if self.__price <= 0:
            print("Цена не должна быть нулевая или орицательная")

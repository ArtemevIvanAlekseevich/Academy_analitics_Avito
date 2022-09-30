import keyword


class ColorizeMixin:
    """Mixin which change text color in terminal"""

    def color_change(self, color_code):
        print(f'\033[0;{color_code};40m', end='')


class SubAttribute:
    """This class helps to create sub attribute of main attribute"""

    def __init__(self, data: dict) -> None:
        for attribute, content in data.items():
            self.attribute_creater(attribute, content)

    def attribute_creater(self, attribute, content) -> None:
        """This function creates dynamic attribute"""
        if keyword.iskeyword(attribute):
            attribute += '_'
        if isinstance(content, dict):
            self.__dict__[attribute] = SubAttribute(content)
        else:
            self.__dict__[attribute] = content


class Advert(ColorizeMixin):
    """Create new advert with dynamic attribute"""
    repr_color_code = 33

    def __init__(self, data: dict = {}) -> None:
        self._price = 0
        for attribute, content in data.items():
            self.attribute_creater(attribute, content)

    def __repr__(self):
        """To change color chande Advert.repr_color_code"""
        super().color_change(Advert.repr_color_code)
        return f'{self.title} | {self.price} ₽'

    def attribute_creater(self, attribute, content) -> None:
        """This function creates dynamic attribute"""
        if attribute == 'price':
            self.price = content
        if keyword.iskeyword(attribute):
            attribute += '_'
        if isinstance(content, dict):
            self.__dict__[attribute] = SubAttribute(content)
        else:
            self.__dict__[attribute] = content

    @property
    def price(self):
        """Cannot be less zero"""
        return self._price

    @price.setter
    def price(self, price):
        """Checking that price is more than zero"""
        if price < 0:
            raise ValueError(': must be >= 0')
        self._price = price
        pass

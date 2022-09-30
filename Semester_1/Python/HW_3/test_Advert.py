import json

import pytest

from Advert import Advert


def test_attribute_creater():
    data = {
        'title': 'Вельш-корги',
        'price': 1000,
        'location': {
            'address': 'Поселок Тишково, 25',
            'metro_stations': {
                'station_orange': ['red', 'orange'],
                'station_apple': ['red', 'green']
            }
        }
    }
    corgi = Advert(data)
    assert corgi.title == 'Вельш-корги'
    assert corgi.location.address == 'Поселок Тишково, 25'
    assert corgi.location.metro_stations.station_orange[1] == 'orange'
    assert corgi.location.metro_stations.station_apple[0] == 'red'


def test_keyword_attribute():
    data = {
        'title': 'Вельш-корги',
        'price': 1000,
        'class': 'dogs',
        'global': 'animal'
    }
    corgi = Advert(data)
    assert 'class_' in corgi.__dict__
    assert corgi.class_ == 'dogs'
    assert 'global' not in corgi.__dict__


def test_empty_instance():
    empty_advert = Advert()
    assert list(empty_advert.__dict__.keys()) == ['_price']


def test_instance_without_price():
    data = {
        'title': 'Вельш-корги',
        'address': 'Поселок Тишково, 25'
    }
    corgi = Advert(data)
    assert corgi.price == 0


def test_price_below_zero():
    data = {
        'title': 'Вельш-корги',
        'price': -1,
        'class': 'dogs'
    }
    try:
        Advert(data)
    except ValueError:
        pass
    else:
        assert False


def test_color():
    """This test isn't auto. Need to check in terminal"""
    data_json = """{
        "title": "python",
        "price": 10,
        "class": {
            "def": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }"""
    data = json.loads(data_json)
    python = Advert(data)
    print(python)
    print('line above should be Yellow')
    Advert.repr_color_code = 37
    print(python)
    print('line above should be White')
    Advert.repr_color_code = 33


if __name__ == '__main__':
    pytest.main()
    test_color()

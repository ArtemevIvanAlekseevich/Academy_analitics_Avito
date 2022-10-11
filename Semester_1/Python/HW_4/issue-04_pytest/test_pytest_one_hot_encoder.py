import pytest

from one_hot_encoder import fit_transform


def test_1_cities():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)
    assert transformed_cities == exp_transformed_cities


def test_2_numbers_order():
    """
    Test checks that the element number is determined only
    by the first occurrence in the sequence.
    """
    cities_1 = ['New York', 'Moscow', 'Moscow', 'Moscow', 'London',
                'Ufa', 'Seoul', 'Seoul', 'Ufa', 'Berlin']
    cities_2 = ['New York', 'Moscow', 'Moscow', 'London', 'Ufa',
                'Seoul', 'Berlin', 'Ufa', 'Seoul', 'Moscow']
    transformed_cities_1 = fit_transform(cities_1)
    transformed_cities_2 = fit_transform(cities_2)
    assert len(transformed_cities_1) == len(transformed_cities_2)
    for city in transformed_cities_1:
        assert city in transformed_cities_2


def test_3_one_type_arguments():
    colors = ['blue', 'blue', 'blue']
    result = fit_transform(colors)
    exp_result = [('blue', [1]), ('blue', [1]), ('blue', [1])]
    assert result == exp_result


def test_4_no_arguments():
    exception = TypeError
    with pytest.raises(exception):
        fit_transform()


def test_5_one_argument():
    color = 'white'
    result = fit_transform(color)
    exp_result = [('white', [1])]
    assert result == exp_result


if __name__ == '__main__':
    pytest.main(['issue-04_pytest/test_pytest_one_hot_encoder.py', '-v'])

import unittest

from one_hot_encoder import fit_transform


class TestOneNotEncoder(unittest.TestCase):
    def test_1_cities(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_2_numbers_order(self):
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
        self.assertCountEqual(transformed_cities_1, transformed_cities_2)

    def test_3_one_type_arguments(self):
        colors = ['blue', 'blue', 'blue']
        result = fit_transform(colors)
        exp_result = [('blue', [1]), ('blue', [1]), ('blue', [1])]
        self.assertEqual(result, exp_result)

    def test_4_no_arguments(self):
        exception = TypeError
        text = 'expected at least 1 arguments, got 0'
        self.assertRaisesRegex(exception, text, fit_transform)

    def test_5_one_argument(self):
        color = 'white'
        result = fit_transform(color)
        exp_result = [('white', [1])]
        self.assertEqual(result, exp_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)

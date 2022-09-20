import unittest

from CountVectorizer import CountVectorizer


class TestCountVectorizer(unittest.TestCase):

    def setUp(self):
        self.vectorizer = CountVectorizer()

    def test_fit_transform(self):
        corpus = [
            'Crock Pot Pasta Never boil pasta again',
            'Pasta Pomodoro Fresh ingredients Parmesan to taste'
        ]
        correct_matrix = [
            [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
        ]
        correct_feature_names = [
            'crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
            'fresh', 'ingredients', 'parmesan', 'to', 'taste'
        ]
        count_matrix = self.vectorizer.fit_transform(corpus)
        feature_names = self.vectorizer.get_feature_names()
        for ind, name in enumerate(correct_feature_names):
            index = feature_names.index(name)
            self.assertEqual(feature_names[index], name)
            for num_doc in range(len(correct_matrix)):
                self.assertEqual(correct_matrix[num_doc][ind],
                                 count_matrix[num_doc][index])

    def test_get_feature_names(self):
        corpus = [
            'Crock Pot Pasta Never boil pasta again',
            'Pasta Pomodoro Fresh ingredients Parmesan to taste'
        ]
        correct_feature_names = [
            'crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
            'fresh', 'ingredients', 'parmesan', 'to', 'taste'
        ]
        self.vectorizer.corpus = corpus
        feature_names = self.vectorizer.get_feature_names()
        self.assertCountEqual(correct_feature_names, feature_names)


if __name__ == '__main__':
    unittest.main()

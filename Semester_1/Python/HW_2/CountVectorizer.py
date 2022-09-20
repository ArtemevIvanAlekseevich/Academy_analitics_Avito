class CountVectorizer():
    """
    Convert collection of documents to document-term matrix
    with feature names
    """

    def __init__(self):
        self.feature_names = list()
        self.corpus = list()

    def fit_transform(self, corpus: list) -> list:
        """Return document-term matrix from given collection of documents"""
        self.corpus = corpus
        self.get_feature_names()
        matrix = []
        for doc in self.corpus:
            list_doc = doc.lower().split()
            matrix.append([])
            for name in self.feature_names:
                matrix[-1].append(0)
                for word in list_doc:
                    if word == name:
                        matrix[-1][-1] += 1
        return matrix

    def get_feature_names(self) -> list:
        """Return list of feature names"""
        if not self.feature_names:
            feature_names = set()
            for doc in self.corpus:
                list_doc = doc.lower().split()
                feature_names.update(list_doc)
            self.feature_names = list(feature_names)
        return self.feature_names


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)

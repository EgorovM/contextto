from navec import Navec
import numpy as np

from django.conf import settings
from sklearn.metrics.pairwise import cosine_distances


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class WordGuesser(metaclass=Singleton):
    def __init__(self, word: str) -> None:
        self._navec = Navec.load(settings.BASE_DIR / 'models/navec_hudlit_v1_12B_500K_300d_100q.tar')
        self._word = word
        self._words = set(self._navec.vocab.words)
        distances = cosine_distances(np.array([self._navec[self._word]]), np.array([
            self._navec[word]
            for word in self._words
        ]))[0]

        self._word_distances = sorted(zip(distances, self._words))
        self._word2order = {word: i for i, (_, word) in enumerate(self._word_distances)}

    @property
    def word_count(self):
        return len(self._words)

    def has_word(self, word: str) -> bool:
        return word in self._words

    def guess(self, word: str) -> int:
        """ Return distance to the provided word """
        return self._word2order[word]
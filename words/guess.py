from navec import Navec
from django.conf import settings
from scipy.spatial.distance import cosine


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class WordGuesser(metaclass=Singleton):
    def __init__(self, word: str = None, words: list[str] = None) -> None:
        self._navec = Navec.load(settings.BASE_DIR / 'models/navec_hudlit_v1_12B_500K_300d_100q.tar')
        self._word = word
        self._words = words or []
        distances = [cosine(self._navec[self._word], self._navec[word]) for word in self._words]
        self._word_distances = sorted(zip(distances, self._words))
        self._word2order = {word: i + 1 for i, (_, word) in enumerate(self._word_distances)}

    @property
    def word_count(self):
        return len(self._words)

    def has_word(self, word: str) -> bool:
        return word in self._words

    def guess(self, word: str) -> int:
        """ Return distance to the provided word """
        return self._word2order[word]

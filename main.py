from abc import ABC, abstractmethod
from pathlib import Path
from cipher import Cipher
from uncipher import Uncipher
import pickle

BASE_DIR = Path(__file__).resolve().parent


class AbstractDataClass(ABC):

    def __init__(self, filepath: str):
        self.filepath = filepath

    @abstractmethod
    def datacipher(self, s: str):
        pass

    @abstractmethod
    def datauncipher(self):
        pass


class DataCipherSave(AbstractDataClass):

    def datacipher(self, s: str):
        with open(self.filepath, "wb") as f:
            pickle.dump(s, f)

    def datauncipher(self):
        with open(self.filepath, "rb") as f:
            return pickle.load(f)


if __name__ == '__main__':
    s = input()
    k = int(input())
    c = Cipher(s, k)
    se = DataCipherSave(str(BASE_DIR.joinpath('secr.pickle')))
    se.datacipher(c)
    print(c)
    r = se.datauncipher()
    r1 = Uncipher(str(r), k)
    print(r1)

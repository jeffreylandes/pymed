from typing import List

from readers.matroska.types.SeekHead import Seek


class SeekHead:
    def __init__(self, seeks: List[Seek]):

        self.seeks = seeks
from typing import List

from readers.matroska.matroska_types.SeekHead.Seek import Seek


class SeekHead:
    def __init__(self, seeks: List[Seek]):

        self.seeks = seeks

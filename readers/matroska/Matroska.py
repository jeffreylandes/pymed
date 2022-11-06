from typing import List

from readers.matroska.types import EBMLDocument


class Matroska:
    def __init__(self, documents: List[EBMLDocument]):

        self.documents = documents

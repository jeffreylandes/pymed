from typing import List

from readers.matroska.matroska_types.EBMLDocument import EBMLDocument


class Matroska:
    def __init__(self, documents: List[EBMLDocument]):

        self.documents = documents

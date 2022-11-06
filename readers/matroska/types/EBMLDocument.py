from readers.matroska.types import Segment, EBMLHeader


class EBMLDocument:
    def __init__(self, header: EBMLHeader, segment_root: Segment):

        self.header = header
        self.segment_root = segment_root

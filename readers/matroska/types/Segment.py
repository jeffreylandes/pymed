from typing import Optional

from readers.matroska.types.Attachments import Attachments
from readers.matroska.types.Chapters import Chapters
from readers.matroska.types.Cluster import Cluster
from readers.matroska.types.Cues import Cues
from readers.matroska.types.Info.Info import Info
from readers.matroska.types.SeekHead.SeekHead import SeekHead
from readers.matroska.types.Tags import Tags
from readers.matroska.types.Tracks import Tracks


class Segment:
    def __init__(
        self,
        seek_head: Optional[SeekHead],
        info: Optional[Info],
        tracks: Optional[Tracks],
        chapters: Optional[Chapters],
        cluster: Optional[Cluster],
        cues: Optional[Cues],
        attachments: Optional[Attachments],
        tags: Optional[Tags],
    ):
        pass

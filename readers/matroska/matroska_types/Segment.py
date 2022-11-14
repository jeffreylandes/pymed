from typing import Optional

from readers.matroska.matroska_types.Attachments import Attachments
from readers.matroska.matroska_types.Chapters import Chapters
from readers.matroska.matroska_types.Cluster.Cluster import Cluster
from readers.matroska.matroska_types.Cues import Cues
from readers.matroska.matroska_types.Info.Info import Info
from readers.matroska.matroska_types.SeekHead.SeekHead import SeekHead
from readers.matroska.matroska_types.Tags import Tags
from readers.matroska.matroska_types.Tracks import Tracks


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

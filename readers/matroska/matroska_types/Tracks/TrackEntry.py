from typing import Optional

from readers.matroska.matroska_types.Tracks.VideoTrack import VideoTrack
from readers.matroska.matroska_types.Tracks.AudioTrack import AudioTrack


class TrackEntry:
    def __init__(
        self,
        track_number: int,
        track_uuid: str,
        track_type: str,
        name: str,
        language: str,
        codec_id: str,
        codec_private: None,
        codec_name: str,
        video: Optional[VideoTrack],
        audio: Optional[AudioTrack],
    ):
        pass

from typing import Optional

from readers.matroska.types.Tracks import VideoTrack, AudioTrack


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

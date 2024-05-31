import os
from typing import List

class VideoCollage:
    def __init__(self, directory_path: str = "./", videofile_pattern: str = "crop_", video_format: str = ".mp4"):
        self.directory_path: str = directory_path
        self.videofile_pattern: str = videofile_pattern
        self.video_format: str = video_format
        self.video_files: List[str] = self.get_videos_from_path()

    def get_videos_from_path(self) -> List[str]:
        videos = [f for f in os.listdir(self.directory_path) if f.endswith(self.video_format) and f.startswith(self.videofile_pattern)]
        #print(videos)
        return videos

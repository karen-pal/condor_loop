import os
from typing import List, Union

class VideoCollage:
    def __init__(self, mix: bool = False, directory_path: Union[str, List[str]] = "./", videofile_pattern: str = "crop_", video_format: str = ".mp4"):
        self.mix = mix
        self.directory_path: Union[str, List[str]] = directory_path
        self.videofile_pattern: str = videofile_pattern
        self.video_format: str = video_format
        self.video_files: List[str] = self.get_videos_from_path()

    def get_videos_from_path(self) -> List[str]:
        
        if self.mix:
            result = []
            videos = [f for f in os.listdir(self.directory_path[0]) if f.endswith(self.video_format) and f.startswith(self.videofile_pattern)]
            result += videos[:len(videos)//2]
            videos = [f for f in os.listdir(self.directory_path[1]) if f.endswith(self.video_format) and f.startswith(self.videofile_pattern)]
            result += videos[len(videos)//2:]
        else:
            result = [f for f in os.listdir(self.directory_path) if f.endswith(self.video_format) and f.startswith(self.videofile_pattern)]
            print(result)
            print(self.directory_path)
        return result

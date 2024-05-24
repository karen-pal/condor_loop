import os
import mpv
import pyautogui
import subprocess
from threading import Timer
import time

DEBUG=False
class VideoPlayer():
    def __init__(self, directory_path="./", videofile_pattern="crop_", video_format=".mp4"):
        self.directory_path = directory_path
        self.videofile_pattern = videofile_pattern
        self.video_format = video_format
        self.video_files = []

    def get_videos_from_path(self):
        self.video_files = [f for f in os.listdir(self.directory_path) if f.endswith(self.video_format) and f.startswith(self.videofile_pattern)]

    def play(self):
        video_processes = []
        mpv_players = []

        self.get_videos_from_path()


        try:
            pyautogui.FAILSAFE = False

            # Get screen size
            screen_width, screen_height = pyautogui.size()

            for i,video_file in enumerate(self.video_files):
                filename = os.path.join(self.directory_path, video_file)
                x_y = filename.split('_')[2:4]
                print(x_y)
                x = int(x_y[0])
                y = int(x_y[1].split(".")[0])
                print(x,y)


                mpv_command = [
                    "mpv",
                    filename,
                    #"--no-audio",  # Mute audio
                    #"--autofit=1920x1080",  # Adjust to your desired video dimensions
                    "--autofit=640x360", #1920x1080",  # Adjust to your desired video dimensions
                    f"--geometry={x}:{y}",  # Set the window position
                    "--on-all-workspaces",
                    "--keep-open=no",  # Close mpv when playback ends
                    "--no-osc",  # Disable on-screen controller
                    "--loop",  # Disable on-screen controller
                    "--no-input-default-bindings",  # Disable default input bindings
                    "--no-border"  # Hide the video outline
                ]
                print("\n")
                print("\n")
                mpv_process = subprocess.Popen(mpv_command, stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

                video_processes.append(mpv_process)
                if DEBUG:
                    if i > 2:
                        break
                    return
            print("\n")
            print("\n")
            playback_duration = 10  # Time in seconds
            time.sleep(playback_duration)
        except KeyboardInterrupt:
            pass

        finally:
            pyautogui.FAILSAFE = True
            for process in video_processes:
                process.terminate()
                process.wait()

if __name__ == "__main__":
    player = VideoPlayer()
    player.play()


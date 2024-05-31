import os
import mpv
import pyautogui
import subprocess
from threading import Timer
import time

DEBUG=False
BUG=False

class VideoPlayer():
    def __init__(self, *, video_collage ):
        self.video_collage = video_collage

    def get_coordinates(self, video_file):
        """ 
        expects a video path str that looks like crop_123_4567.mp4
        """
        x_y = video_file.split('_')[2:4]
        if DEBUG:
            print("x_Y")
            print(x_y)
        x = int(x_y[0])
        y = int(x_y[1].split(".")[0])
        if DEBUG:
            print(x,y)
        return x,y

    def play(self):
        video_processes = []
        mpv_players = []

        try:
            pyautogui.FAILSAFE = False

            # Get screen size
            screen_width, screen_height = pyautogui.size()
            print(self.video_collage.video_files)
            for i,video_file in enumerate(self.video_collage.video_files):
                if self.video_collage.mix == True:
                    if i < len(self.video_collage.video_files)//2:
                        full_path = os.path.join(self.video_collage.directory_path[0], video_file)
                    else:
                        full_path = os.path.join(self.video_collage.directory_path[1], video_file)
                else:
                    full_path = os.path.join(self.video_collage.directory_path, video_file)
                x,y = self.get_coordinates(video_file)

                print(full_path)
                mpv_command = [
                    "mpv",
                    full_path,
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
                if DEBUG:
                    print("\n")
                    print("\n")
                mpv_process = subprocess.Popen(mpv_command, stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

                video_processes.append(mpv_process)
                if BUG:
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


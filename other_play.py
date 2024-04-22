import os
import mpv
import pyautogui
import subprocess


def play_videos(directory_path):
    video_processes = []
    video_files = [f for f in os.listdir(directory_path) if f.endswith('.mp4') and f.startswith('crop_')]

    mpv_players = []

    try:
        pyautogui.FAILSAFE = False

        # Get screen size
        screen_width, screen_height = pyautogui.size()

        for i,video_file in enumerate(video_files):
            filename = os.path.join(directory_path, video_file)
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
            mpv_process = subprocess.Popen(mpv_command, stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            video_processes.append(mpv_process)

        input("Press Enter to quit...")

    except KeyboardInterrupt:
        pass

    finally:
        pyautogui.FAILSAFE = True
        #for player in mpv_players:
        #    player.terminate()

if __name__ == "__main__":
    play_videos("./")


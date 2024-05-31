Laura, Say hello to my little video looper


<img src="screen.png">


Made with AMOR using python, by Karen Palacio.

> For a very custom type of video.

# Contents

- workflow to generate img2video using ComfyUI 
- other_play.py : quick PoC script version of the sequencer
- sequencer.py : sequencer WIP - meant to run for a collection of videos
- video_player: video player class that uses mpv - meant for a single video

# Dependencies
pip install mpv-python pyautogui


# Usage
## quick & dirty usage (this will not work on your computer)
python3 other_play.py

## actual usage
### with sequencing:
python3 sequencer.py

### without sequencing:
python3 video_player.py

from video_player import VideoPlayer 
from video_collage import VideoCollage
from time import sleep

class Sequence():
    """a sequence needs the values of slots
    then, a sequence is made of a pattern
    of a certain length
    """
    def __init__(self, ):
        self.pattern = "1-2"
        self.data = {0:"./videos/videos_frame_2136",1:"./videos/videos_frame_2184",2:"./videos/videos_frame_2232"}

    def run(self):
        for i,val in enumerate(self.pattern):
            print(i,val)
            if val == "-":
                print("-")
                sleep(2)
            else:
                print(">>>*")
                collage = VideoCollage(self.data[i])
                VideoPlayer(video_collage=collage).play()
                sleep(2)
            

seq = Sequence()
seq.run()

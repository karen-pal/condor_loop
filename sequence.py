from video_player import VideoPlayer 
from video_collage import VideoCollage
from time import sleep

class Sequence():
    """ given slots and a pattern
    of a certain length, you program
    a sequence of videos to be played
    in that order
    """
    def __init__(self, ):
        self.pattern = "01~"
        self.data = {0:"./videos/videos_frame_2136",1:"./videos/videos_frame_2184",2:"./videos/videos_frame_2232"}
        self.mix_config = {0:[],1:[],2:[self.data[0],self.data[1]]}  

    def validate_mix_config(self):
        """ 
        for config in mix_config:
                len(config) <= 2
                len(self.mix_config) == len(self.pattern)

        """
        return True
    def run(self):
        if not self.validate_mix_config():
            return

        for i,val in enumerate(self.pattern):
            print(i,val)
            if val == "-":
                print("- no play")
                sleep(2)
            elif val == "~":
                print(">>>~mix")
                mix_config = self.mix_config[i]
                collage = VideoCollage(mix=True, directory_path=mix_config)
                VideoPlayer(video_collage=collage).play()
                sleep(2)
                
            else:
                print(">>>*single play")
                collage = VideoCollage(directory_path=self.data[i])
                VideoPlayer(video_collage=collage).play()
                sleep(2)
            
#eventualmente en tiempo de ejecución mix() será una operación en caliente y no de config
seq = Sequence()
seq.run()

from video_player import VideoPlayer 
from time import sleep

class Sequence():
    """a sequence needs the values of slots
    then, a sequence is made of a pattern
    of a certain length
    """
    def __init__(self, ):
        self.pattern = "*--"
        self.data = ["./","./","./"]

    def run(self):
        for i,val in enumerate(self.pattern):
            print(i,val)
            if val == "*":
                print(">>>*")
                VideoPlayer(self.data[i]).play()
                sleep(2)
            else:
                print("-")
                sleep(2)
            

seq = Sequence()
seq.run()

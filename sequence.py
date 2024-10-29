from video_player import VideoPlayer 
from video_collage import VideoCollage
from time import sleep

# racimos
corridor = "/home/frontera/Documents/Projects/condor_loop/sensorialis/corridor/scaled_video_crops"
malvinas ="/home/frontera/Documents/Projects/condor_loop/sensorialis/malvinas_127/scaled_video_crops"
coleccion_malvinas ="/home/frontera/Documents/Projects/condor_loop/sensorialis/coleccion_malvinas2/scaled_video_crops"
coleccion_malvinas2 ="/home/frontera/Documents/Projects/condor_loop/sensorialis/corridor2/scaled_video_crops" 
jarra = "/home/frontera/Documents/Projects/condor_loop/sensorialis/jarra/scaled_video_crops"
reconstruccion = "/home/frontera/Documents/Projects/condor_loop/sensorialis/reconstruccion/videos"
laura  ="/home/frontera/Downloads/output_folder_crops2/frame_2640/videos/"
biblio ="/home/frontera/Documents/Projects/condor_loop/sensorialis/biblio/videos"
laura2 ="/home/frontera/Downloads/output_folder_crops2/frame_24/videos" 
paisaje="/home/frontera/Downloads/output_folder_crops2/frame_2232/videos"
tronco = "/home/frontera/Documents/Projects/condor_loop/sensorialis/tronco/scaled_video_crops"
blanco = "/home/frontera/Documents/Projects/condor_loop/sensorialis/blanco/scaled_video_crops"
cuba = "/home/frontera/Documents/Projects/condor_loop/sensorialis/cuba/scaled_video_crops"
cuba2 = "/home/frontera/Documents/Projects/condor_loop/sensorialis/cuba2/scaled_video_crops"
fosil = "/home/frontera/Documents/Projects/condor_loop/sensorialis/fosil/scaled_video_crops"
fosil2 = "/home/frontera/Documents/Projects/condor_loop/sensorialis/fosil2/scaled_video_crops"
mostrar = "/home/frontera/Documents/Projects/condor_loop/sensorialis/mostrar/scaled_video_crops"
sueña = "/home/frontera/Documents/Projects/condor_loop/sensorialis/sueña/videos"
sueñaw = "/home/frontera/Documents/Projects/condor_loop/sensorialis/sueña_w/videos"
corridor2 = "/home/frontera/Documents/Projects/condor_loop/sensorialis/corridor2/scaled_video_crops"
cba1 = "/home/frontera/Documents/Projects/condor_loop/sensorialis/cba1/scaled_video_crops"
cba4 = "/home/frontera/Documents/Projects/condor_loop/sensorialis/cba4/scaled_video_crops"


#colecciones
## malvinas
malvinas_collection = {
        0:sueñaw,
        1:malvinas,
        2:coleccion_malvinas,
        3:coleccion_malvinas2,
        5:laura2,
        6:reconstruccion,
        7:laura,
        8:sueña,
        }

full_data={
           0:corridor, 
           1:malvinas,
           2:coleccion_malvinas,
           3:coleccion_malvinas2,
           4:jarra,
           5:reconstruccion,
           6:laura,
           7:biblio,
           8:laura2,
           9:paisaje,
           10:tronco,
           11:blanco,
           12:cuba,
           13:cuba2,
           14:fosil,
           15:fosil2,
           16:mostrar,
           17:sueña,
           18:sueñaw,
           19:corridor2,
           20:cba1,
           21:cba4,
           }

class Sequence():
    """ given slots and a pattern
    of a certain length, you program
    a sequence of videos to be played
    in that order
    """
    def __init__(self ):
        self.pattern = "*"*22 #"01~~45678"
        #self.data = {0:"./videos/videos_frame_2136",1:"./videos/videos_frame_2184",2:"./videos/videos_frame_2232"}
        self.data = full_data
        self.mix_config = {
                        0:[],
                        1:[],
                        2:[self.data[0],self.data[1]],
                        3:[self.data[3],self.data[5]],
                        4:[],
                        5:[],
                        6:[],
                        7:[],
                        8:[],
                        9:[],
                        10:[],
                        11:[],
                        12:[],
                        13:[],
                        14:[],
                        15:[],
                        16:[],
                        17:[],
                        18:[],
                        19:[],
                        20:[],
                        21:[],
                        }

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
        while True:
            for i,val in enumerate(self.pattern):

                print(i,val)
                if val == "-":
                    print("- no play")
                    sleep(2)
                elif val == "~":
                    print(">>>~mix")
                    mix_config = self.mix_config[i]
                    print(mix_config)
                    print("\n")
                    collage = VideoCollage(mix=True, directory_path=mix_config)
                    VideoPlayer(video_collage=collage).play()
                    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    sleep(2)
                    
                else:
                    print(">>>*single play")
                    collage = VideoCollage(directory_path=self.data[i])
                    VideoPlayer(video_collage=collage).play()
                    sleep(1)
            
#eventualmente en tiempo de ejecución mix() será una operación en caliente y no de config
seq = Sequence()
seq.run()

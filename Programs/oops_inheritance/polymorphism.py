class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")

        self.filename = filename

class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print("playing {} as mp3".format(self.filename))

class WavFile(AudioFile):
    ext = "wav"
    def play(self):
        print("playing {} as wav".format(self.filename))

class OggFile(AudioFile):
    ext = "ogg"
    def play(self):
        print("playing {} as ogg".format(self.filename))

ogg = OggFile("myfile.ogg")
ogg.play()


mp3 = MP3File("Secondfile.mp3")
mp3.play()

ttrs = vars(mp3)
print (ttrs)

ttrs = vars(ogg)
print (ttrs)

''' belo code will throw an exception 
mp3 = MP3File("Thirdfile.avi")
mp3.play() 
Uncomment this and check
'''


''' Assignment:
change the code such that when you chaeck the attribures of a object 
using ttrs = vars(mp3) and vars(ogg) it should print different attributes '''







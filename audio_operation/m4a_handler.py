from pydub import AudioSegment
import speechbrain 
def read_m4a(path):
    audio = AudioSegment.from_file(path, format="m4a")
    
    
class Frame(object):
    def __init__(self, bytes, timestamp, duration):
        self.bytes = bytes
        self.timestamp = timestamp
        self.duration = duration
        
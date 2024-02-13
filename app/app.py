from pydub import AudioSegment

def convertWavToMp3(wavFile, mp3File):
    # ffmpeg = "/opt/homebrew/Cellar/ffmpeg/6.0/bin/ffmpeg"
    ffmpegPath = "/opt/homebrew/Cellar/ffmpeg/6.0/bin/ffmpeg.exe"
    AudioSegment.ffmpeg = ffmpegPath
    audio = AudioSegment.from_wav(wavFile)
    audio.export(mp3File, format="mp3")
    
wavLocation = "./amor_o_costumbre.wav"
mp3Destination = "./amor_o_costumbre.mp3"

convertWavToMp3(wavLocation, mp3Destination)
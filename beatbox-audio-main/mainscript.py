import os
from os.path import exists
os.environ["PATH"]="/usr/local/lib/python3.9/site-packages/" + os.environ.get("PATH","")
import sys
sys.path.append('/usr/local/lib/python3.9/site-packages/')
import ffmpeg
from pydub import AudioSegment
from moviepy.editor import VideoFileClip
from pedalboard import Pedalboard, Compressor, Gain, LowShelfFilter, HighShelfFilter, NoiseGate, Limiter, Distortion, Mix, Reverb, load_plugin, HighpassFilter, LowpassFilter, PeakFilter
from pedalboard.io import AudioFile
from pydub.utils import mediainfo
os.environ["PATH"]+= os.pathsep + "usr/bin/ffprobe"

# Audio conversion and extraction functions
def convert_audio_to_wav(input_file, ext):
    audio = AudioSegment.from_file(input_file)
    output_file = input_file.rsplit(".", 1)[0] + ".wav"
    print("converts Audio")
    audio.export(output_file, format="wav")
    return output_file

def extract_audio_from_video(video_file):
    video = VideoFileClip(video_file)
    audio = video.audio
    output_file = video_file.rsplit(".", 1)[0] + ".wav"
    audio.write_audiofile(output_file, codec='pcm_s16le')  # .wav format
    return output_file

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

def replace_audio_in_video(video_file, new_audio_file, output_video_file):
    video = VideoFileClip(video_file)
    new_audio = AudioFileClip(new_audio_file)
    video_with_new_audio = video.set_audio(new_audio)
    video_with_new_audio.write_videofile(output_video_file, codec='libx264')

# Input
input_file = str(sys.argv[1])
outputpath = "audiofiles/"
mic = sys.argv[2] == "True"
style = str(sys.argv[3])
filename = input_file.rsplit("/", 1)[-1]

filename_parts = filename.rsplit(".", 1)
file_name = filename_parts[0]
file_extension = filename_parts[1] if len(filename_parts) > 1 else ""
# Handle audio conversion and extraction
# do a condition for wav maybe?
if file_extension != "wav":
	cmd = "/usr/bin/ffmpeg -i {0} {1}".format(outputpath + filename, outputpath + file_name + ".wav")
	code = os.system(cmd)

sound = AudioSegment.from_wav(outputpath + file_name + ".wav")
sound = sound.set_channels(1)
normalized_file_name = outputpath + file_name + "--Normalised" + ".wav"
normalized_file = match_target_amplitude(sound, -26.0)
normalized_file.export(normalized_file_name, format="wav")
print('outputted normalized')
with AudioFile(normalized_file_name) as f:
    audio = f.read(f.frames)
    samplerate = f.samplerate
normalized_file_name = outputpath + file_name + "--processed" + ".wav"
# Chains
def bassheavy():

    Low = Pedalboard([
                 NoiseGate(threshold_db=-50,ratio=4,attack_ms=3,release_ms=35),
                 Gain(gain_db=-95),
                 Compressor(threshold_db=-85, ratio=30,attack_ms=20,release_ms=100),
                 HighpassFilter(cutoff_frequency_hz=35),
                 LowpassFilter(cutoff_frequency_hz=200),
                 Limiter(threshold_db=-85)

         ])
    Mid = Pedalboard([
                 NoiseGate(threshold_db=-50,ratio=4,attack_ms=3,release_ms=35),
                 Gain(gain_db=-95.0),
                 Compressor(threshold_db=-60, ratio=20,attack_ms=20,release_ms=100),
                 HighpassFilter(cutoff_frequency_hz=200),
                 LowpassFilter(cutoff_frequency_hz=3500),
                 PeakFilter(cutoff_frequency_hz = 800, gain_db = -25, q = 2.1),
                 Limiter(threshold_db=-65)                  
         ])
    High = Pedalboard([
                 NoiseGate(threshold_db=-50,ratio=4,attack_ms=3,release_ms=35),
                 Gain(gain_db=-85.0),
                 Compressor(threshold_db=-60, ratio=20,attack_ms=20,release_ms=100),
                 HighpassFilter(cutoff_frequency_hz=3500),
                 LowpassFilter(cutoff_frequency_hz=13000),
                 PeakFilter(cutoff_frequency_hz = 10000, gain_db = -25, q = 2.1),
                 Limiter(threshold_db=-65)                         
         ])
            

    ReverbChain = Pedalboard([
         Reverb(room_size=1, damping=1, wet_level=0.01,dry_level=1,width=0),
         HighpassFilter(cutoff_frequency_hz=350)
         ])
    MASTER = Pedalboard([
                 NoiseGate(threshold_db=-40,ratio=4,attack_ms=3,release_ms=35),
                 Compressor(threshold_db=0, ratio=20,attack_ms=20,release_ms=100),
                 PeakFilter(cutoff_frequency_hz = 80, gain_db = 15, q = 2.1),
                 PeakFilter(cutoff_frequency_hz = 5000, gain_db = 25, q = 1.5),
                 PeakFilter(cutoff_frequency_hz = 9000, gain_db = 15, q = 2.1),
		         PeakFilter(cutoff_frequency_hz = 30, gain_db = 20, q = 1.5),
                 LowpassFilter(cutoff_frequency_hz=16500),
                 Limiter(threshold_db=3)                        
         ])
    LMH = Pedalboard([Mix([Low, Mid, High])])
    REV = Pedalboard([Mix([LMH,ReverbChain])])
    MAS = Pedalboard([Mix([REV,MASTER])])
    effected = MAS(audio, samplerate)

    with AudioFile(normalized_file_name, 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)
    print('wrote out processed file')


def musical():

    Low = Pedalboard([
                 NoiseGate(threshold_db=-50,ratio=4,attack_ms=3,release_ms=35),
                 Gain(gain_db=-95),
                 Compressor(threshold_db=-80, ratio=30,attack_ms=20,release_ms=100),
                 HighpassFilter(cutoff_frequency_hz=35),
                 LowpassFilter(cutoff_frequency_hz=200),
                 Limiter(threshold_db=-75)

         ])
    Mid = Pedalboard([
                 NoiseGate(threshold_db=-50,ratio=4,attack_ms=3,release_ms=35),
                 Gain(gain_db=-85.0),
                 Compressor(threshold_db=-40, ratio=20,attack_ms=20,release_ms=100),
                 HighpassFilter(cutoff_frequency_hz=200),
                 LowpassFilter(cutoff_frequency_hz=3500),
                 PeakFilter(cutoff_frequency_hz = 800, gain_db = -25, q = 2.1),
                 Limiter(threshold_db=-55)                  
         ])
    High = Pedalboard([
                 NoiseGate(threshold_db=-50,ratio=4,attack_ms=3,release_ms=35),
                 Gain(gain_db=-85.0),
                 Compressor(threshold_db=-40, ratio=20,attack_ms=20,release_ms=100),
                 HighpassFilter(cutoff_frequency_hz=3500),
                 LowpassFilter(cutoff_frequency_hz=13000),
                 PeakFilter(cutoff_frequency_hz = 10000, gain_db = -25, q = 2.1),
                 Limiter(threshold_db=-55)                         
         ])
            

    ReverbChain = Pedalboard([
         Reverb(room_size=0.25, damping=0.25, wet_level=0.21, dry_level=0.50, width=0.25),
         HighpassFilter(cutoff_frequency_hz=350)
         ])
    MASTER = Pedalboard([
                 NoiseGate(threshold_db=-40,ratio=4,attack_ms=3,release_ms=35),
                 Compressor(threshold_db=0, ratio=20,attack_ms=20,release_ms=100),
                 PeakFilter(cutoff_frequency_hz = 80, gain_db = 15, q = 2.1),
                 PeakFilter(cutoff_frequency_hz = 5000, gain_db = 28, q = 1.5),
                 PeakFilter(cutoff_frequency_hz = 9000, gain_db = 18, q = 2.1),
                 PeakFilter(cutoff_frequency_hz = 30, gain_db = 20, q = 1.5),
                 LowpassFilter(cutoff_frequency_hz=16500),
                 Limiter(threshold_db=3)                        
         ])
    LMH = Pedalboard([Mix([Low, Mid, High])])
    REV = Pedalboard([Mix([LMH,ReverbChain])])
    MAS = Pedalboard([Mix([REV,MASTER])])
    effected = MAS(audio, samplerate)

    with AudioFile(normalized_file_name, 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)
    print('wrote out processed file')

def technical():

    Low = Pedalboard([
                 NoiseGate(threshold_db=-50,ratio=4,attack_ms=3,release_ms=35),
                 Gain(gain_db=-105),
                 Compressor(threshold_db=-80, ratio=30,attack_ms=20,release_ms=100),
                 HighpassFilter(cutoff_frequency_hz=35),
                 LowpassFilter(cutoff_frequency_hz=200),
                 Limiter(threshold_db=-75)

         ])
    Mid = Pedalboard([
                 NoiseGate(threshold_db=-50,ratio=4,attack_ms=3,release_ms=35),
                 Gain(gain_db=-95.0),
                 Compressor(threshold_db=-70, ratio=20,attack_ms=20,release_ms=100),
                 HighpassFilter(cutoff_frequency_hz=200),
                 LowpassFilter(cutoff_frequency_hz=3500),
                 PeakFilter(cutoff_frequency_hz = 800, gain_db = -25, q = 2.1),
                 Limiter(threshold_db=-75)                  
         ])
    High = Pedalboard([
                 NoiseGate(threshold_db=-50,ratio=4,attack_ms=3,release_ms=35),
                 Gain(gain_db=-85.0),
                 Compressor(threshold_db=-70, ratio=20,attack_ms=20,release_ms=100),
                 HighpassFilter(cutoff_frequency_hz=3500),
                 LowpassFilter(cutoff_frequency_hz=13000),
                 PeakFilter(cutoff_frequency_hz = 10000, gain_db = -25, q = 2.1),
                 Limiter(threshold_db=-75)                         
         ])
            

    ReverbChain = Pedalboard([
         Reverb(room_size=1, damping=1, wet_level=0.01,dry_level=1,width=0),
         HighpassFilter(cutoff_frequency_hz=350)
         ])
    MASTER = Pedalboard([
                 NoiseGate(threshold_db=-40,ratio=4,attack_ms=3,release_ms=35),
                 Compressor(threshold_db=0, ratio=20,attack_ms=20,release_ms=100),
                 PeakFilter(cutoff_frequency_hz = 80, gain_db = 15, q = 2.1),
                 PeakFilter(cutoff_frequency_hz = 5000, gain_db = 25, q = 1.5),
                 PeakFilter(cutoff_frequency_hz = 9000, gain_db = 15, q = 2.1),
                 PeakFilter(cutoff_frequency_hz = 30, gain_db = 20, q = 1.5),
                 LowpassFilter(cutoff_frequency_hz=16500),
                 Limiter(threshold_db=3)                        
         ])
    LMH = Pedalboard([Mix([Low, Mid, High])])
    REV = Pedalboard([Mix([LMH,ReverbChain])])
    MAS = Pedalboard([Mix([REV,MASTER])])
    effected = MAS(audio, samplerate)

    with AudioFile(normalized_file_name, 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)
    print('wrote out processed file')

def bassheavy_phone():

    Low = Pedalboard([
                 NoiseGate(threshold_db=-50,ratio=4,attack_ms=3,release_ms=35),
                 Gain(gain_db=-95),
                 Compressor(threshold_db=-80, ratio=30,attack_ms=20,release_ms=100),
                 HighpassFilter(cutoff_frequency_hz=35),
                 LowpassFilter(cutoff_frequency_hz=200),
                 Limiter(threshold_db=-85)

         ])
    Mid = Pedalboard([
                 NoiseGate(threshold_db=-50,ratio=4,attack_ms=3,release_ms=35),
                 Gain(gain_db=-95.0),
                 Compressor(threshold_db=-60, ratio=20,attack_ms=20,release_ms=100),
                 HighpassFilter(cutoff_frequency_hz=200),
                 LowpassFilter(cutoff_frequency_hz=3500),
                 PeakFilter(cutoff_frequency_hz = 800, gain_db = -25, q = 2.1),
                 Limiter(threshold_db=-65)                  
         ])
    High = Pedalboard([
                 NoiseGate(threshold_db=-50,ratio=4,attack_ms=3,release_ms=35),
                 Gain(gain_db=-85.0),
                 Compressor(threshold_db=-60, ratio=20,attack_ms=20,release_ms=100),
                 HighpassFilter(cutoff_frequency_hz=3500),
                 LowpassFilter(cutoff_frequency_hz=13000),
                 PeakFilter(cutoff_frequency_hz = 10000, gain_db = -25, q = 2.1),
                 Limiter(threshold_db=-65)                         
         ])
            

    ReverbChain = Pedalboard([
         Reverb(room_size=1, damping=1, wet_level=0.01,dry_level=1,width=0),
         HighpassFilter(cutoff_frequency_hz=350)
         ])
    MASTER = Pedalboard([
                 NoiseGate(threshold_db=-40,ratio=4,attack_ms=3,release_ms=35),
                 Compressor(threshold_db=0, ratio=20,attack_ms=20,release_ms=100),
                 PeakFilter(cutoff_frequency_hz = 80, gain_db = 15, q = 2.1),
                 PeakFilter(cutoff_frequency_hz = 5000, gain_db = 25, q = 1.5),
                 PeakFilter(cutoff_frequency_hz = 9000, gain_db = 15, q = 2.1),
                 PeakFilter(cutoff_frequency_hz = 30, gain_db = 20, q = 1.5),
                 LowpassFilter(cutoff_frequency_hz=16500),
                 Limiter(threshold_db=3)                        
         ])
    LMH = Pedalboard([Mix([Low, Mid, High])])
    REV = Pedalboard([Mix([LMH,ReverbChain])])
    MAS = Pedalboard([Mix([REV,MASTER])])
    effected = MAS(audio, samplerate)

    with AudioFile(normalized_file_name, 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)
    print('wrote out processed file')

def musical_phone():

    Low = Pedalboard([
                 NoiseGate(threshold_db=-40,ratio=4,attack_ms=3,release_ms=35),
                 Gain(gain_db=6.0),
                 Compressor(threshold_db=40, ratio=30,attack_ms=20,release_ms=100),
                 HighpassFilter(cutoff_frequency_hz=35),
                 LowpassFilter(cutoff_frequency_hz=200),
                 Limiter(threshold_db=-2),
                 PeakFilter(cutoff_frequency_hz = 30, gain_db = -10, q = 2.1)

         ])
    Mid = Pedalboard([
                 NoiseGate(threshold_db=-40,ratio=4,attack_ms=3,release_ms=35),
                 Gain(gain_db=-2.0),
                 Compressor(threshold_db=20, ratio=20,attack_ms=20,release_ms=100),
                 HighpassFilter(cutoff_frequency_hz=200),
                 LowpassFilter(cutoff_frequency_hz=3500),
                 PeakFilter(cutoff_frequency_hz = 800, gain_db = -2, q = 2.1),
                 Limiter(threshold_db=-2)                       
         ])
    High = Pedalboard([
                 NoiseGate(threshold_db=-40,ratio=4,attack_ms=3,release_ms=35),
                 Gain(gain_db=3.0),
                 Compressor(threshold_db=20, ratio=20,attack_ms=20,release_ms=100),
                 HighpassFilter(cutoff_frequency_hz=4000),
                 LowpassFilter(cutoff_frequency_hz=15000),
                 PeakFilter(cutoff_frequency_hz = 13000, gain_db = -2, q = 2.1),
                 Limiter(threshold_db=-2)                         
         ])
            

    ReverbChain = Pedalboard([
         Reverb(room_size=1, damping=1, wet_level=0.2,dry_level=1,width=0),
         ])
    MASTER = Pedalboard([
                 NoiseGate(threshold_db=2,ratio=4,attack_ms=100),
                 Compressor(threshold_db=5, ratio=20,attack_ms=20,release_ms=100),
                 PeakFilter(cutoff_frequency_hz = 80, gain_db = 2, q = 2.1),
                 PeakFilter(cutoff_frequency_hz = 3500, gain_db = 2, q = 2.1),
                 PeakFilter(cutoff_frequency_hz = 9000, gain_db = 2, q = 2.1),
		 PeakFilter(cutoff_frequency_hz = 30, gain_db = -20, q = 2.1),
                 Limiter(threshold_db=-10)                        
         ])
    LMH = Pedalboard([Mix([Low, Mid, High])])
    REV = Pedalboard([Mix([LMH,ReverbChain])])
    MAS = Pedalboard([Mix([REV,MASTER])])
    effected = MAS(audio, samplerate)

    with AudioFile(normalized_file_name, 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)
    print('wrote out processed file')
def technical_phone():

    Low = Pedalboard([
                 NoiseGate(threshold_db=-40,ratio=4,attack_ms=3,release_ms=35),
                 Gain(gain_db=9.0),
                 Compressor(threshold_db=40, ratio=30,attack_ms=20,release_ms=100),
                 HighpassFilter(cutoff_frequency_hz=35),
                 LowpassFilter(cutoff_frequency_hz=200),
                 Limiter(threshold_db=-2),
                 PeakFilter(cutoff_frequency_hz = 30, gain_db = -10, q = 2.1)

         ])
    Mid = Pedalboard([
                 NoiseGate(threshold_db=-40,ratio=4,attack_ms=3,release_ms=35),
                 Gain(gain_db=-2.0),
                 Compressor(threshold_db=20, ratio=20,attack_ms=20,release_ms=100),
                 HighpassFilter(cutoff_frequency_hz=200),
                 LowpassFilter(cutoff_frequency_hz=3500),
                 PeakFilter(cutoff_frequency_hz = 800, gain_db = -2, q = 2.1),
                 Limiter(threshold_db=-2)                       
         ])
    High = Pedalboard([
                 NoiseGate(threshold_db=-40,ratio=4,attack_ms=3,release_ms=35),
                 Gain(gain_db=6.0),
                 Compressor(threshold_db=20, ratio=20,attack_ms=20,release_ms=100),
                 HighpassFilter(cutoff_frequency_hz=4000),
                 LowpassFilter(cutoff_frequency_hz=15000),
                 PeakFilter(cutoff_frequency_hz = 13000, gain_db = -2, q = 2.1),
                 Limiter(threshold_db=-2)                         
         ])
            

    ReverbChain = Pedalboard([
         Reverb(room_size=1, damping=1, wet_level=0,dry_level=1,width=0),
         ])
    MASTER = Pedalboard([
                 NoiseGate(threshold_db=2,ratio=4,attack_ms=100),
                 Compressor(threshold_db=5, ratio=20,attack_ms=20,release_ms=100),
                 PeakFilter(cutoff_frequency_hz = 80, gain_db = 2, q = 2.1),
                 PeakFilter(cutoff_frequency_hz = 3500, gain_db = 2, q = 2.1),
                 PeakFilter(cutoff_frequency_hz = 9000, gain_db = 2, q = 2.1),
		 PeakFilter(cutoff_frequency_hz = 30, gain_db = -20, q = 2.1),
                 Limiter(threshold_db=-10)                        
         ])
    LMH = Pedalboard([Mix([Low, Mid, High])])
    REV = Pedalboard([Mix([LMH,ReverbChain])])
    MAS = Pedalboard([Mix([REV,MASTER])])
    effected = MAS(audio, samplerate)

    with AudioFile(normalized_file_name, 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)
    print('wrote out processed file')
# Process based on mic and style
if mic:
    if style == "bass":
        bassheavy()
    elif style == "music":
        musical()
    elif style == "tech":
        technical()
else:
    if style == "bass":
        bassheavy_phone()
    elif style == "music":
        musical_phone()
    elif style == "tech":
        technical_phone()

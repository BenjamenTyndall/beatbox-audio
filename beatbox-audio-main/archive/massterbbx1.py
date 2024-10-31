# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:29:28 2022

@author: ejhom
"""

from pedalboard import Pedalboard, Compressor, Gain, LowShelfFilter, HighShelfFilter, NoiseGate, Limiter, Distortion,Mix, Reverb, load_plugin, HighpassFilter, LowpassFilter
from pedalboard.io import AudioFile



from pydub import AudioSegment
import sys

#SETUP OF INPUT FILE
#C:\Program Files\Common Files\VST3\Soundtheory
# Read the input file and mic value from the command line arguments
input_file = sys.argv[1]
print(input_file + "file imported")
mic = sys.argv[2]
print(mic + "bool accepted")
style = sys.argv[3]
print(style + "style accepted")

a = input_file.split("/")
b = a[len(a)-1]
c = b.split(".")

print("a")

#vst2 = load_plugin("")
#vst3 = load_plugin("")
#vst4 = load_plugin("")
#vst5 = load_plugin("")

def match_target_amplitude(f, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

print("b")

sound = AudioSegment.from_wav(input_file)
print("c")
sound = sound.set_channels(1)
print("step1")
normalized_file = match_target_amplitude(sound, -26.0)
normalized_file.export((c[0] + "--nomrmalized.wav"), format="wav")
print("step2")
with AudioFile((c[0] + "--nomrmalized.wav")) as f:
  audio = f.read(f.frames)
  samplerate = f.samplerate

print("step3")
def bassheavy():
    vst1 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst1.low_freq_hz = 250
    vst1.low_gain_db = -2
    
    vst2 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst2.low_freq_hz = 500
    vst2.low_gain_db = -2
    
    vst3 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst3.low_freq_hz = 800
    vst3.low_gain_db = -2
    
    vst4 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst4.low_freq_hz = 40
    vst4.low_gain_db = 18
    
    vst5 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst5.low_freq_hz = 80
    vst5.low_gain_db = 13
    
    vst6 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst6.mid_freq_hz = 2500
    vst6.mid_gain_db = 12
    
    vst7 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst7.high_freq_hz = 8000
    vst7.high_gain_db = 18

    
    vst8 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst8.high_freq_hz = 8000
    vst8.high_gain_db = 18
    
    vst9 = load_plugin("C:\Program Files\Common Files\VST3\OTT.vst3")

    vst9.out_gain_db = 1

    compressioncahin = Pedalboard([
                                NoiseGate(threshold_db=-40, ratio = 10, attack_ms = 2),
                                   vst1,vst2,vst3,
                                   Compressor(threshold_db=-20, ratio=3,attack_ms=20,release_ms=100),
                                   vst4,vst5,vst6,vst7, vst8,
                                   
                                 #  vst9,
                                   
                                   Limiter(threshold_db=-1)
                             
                                   
         
         ])
    ReverbChain = Pedalboard([
         Reverb(room_size=.1, damping=1, wet_level=.05,dry_level=1,width=1)
         ])
     
    Full = Pedalboard([Mix([compressioncahin, ReverbChain])])
    
    effected = Full(audio, samplerate)
    
    with AudioFile((c[0] + ".wav"), 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)
    print("File created")
def musical():
    vst1 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst1.low_freq_hz = 250
    vst1.low_gain_db = -2
    
    vst2 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst2.low_freq_hz = 500
    vst2.low_gain_db = -2
    
    vst3 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst3.low_freq_hz = 800
    vst3.low_gain_db = -2
    
    vst4 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst4.low_freq_hz = 40
    vst4.low_gain_db = 18
    
    vst5 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst5.low_freq_hz = 80
    vst5.low_gain_db = 13
    
    vst6 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst6.mid_freq_hz = 2500
    vst6.mid_gain_db = 12
    
    vst7 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst7.high_freq_hz = 8000
    vst7.high_gain_db = 18

    
    vst8 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst8.high_freq_hz = 8000
    vst8.high_gain_db = 18
    
    vst9 = load_plugin("C:\Program Files\Common Files\VST3\OTT.vst3")

    vst9.out_gain_db = 1

    compressioncahin = Pedalboard([
                                NoiseGate(threshold_db=-40, ratio = 10, attack_ms = 2),
                                   vst1,vst2,vst3,
                                   Compressor(threshold_db=-20, ratio=3,attack_ms=20,release_ms=100),
                                   vst4,vst5,vst6,vst7, vst8,
                                   
                                 #  vst9,
                                   
                                   Limiter(threshold_db=-1)
                             
                                   
         
         ])
    ReverbChain = Pedalboard([
         Reverb(room_size=.3, damping=1, wet_level=.1,dry_level=1,width=1)
         ])
     
    Full = Pedalboard([Mix([compressioncahin, ReverbChain])])
    
    effected = Full(audio, samplerate)
    
    with AudioFile((c[0]+ ".wav"), 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)
         
def tech():
    vst1 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst1.low_freq_hz = 250
    vst1.low_gain_db = -2
    
    vst2 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst2.low_freq_hz = 500
    vst2.low_gain_db = -2
    
    vst3 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst3.low_freq_hz = 800
    vst3.low_gain_db = -2
    
    vst4 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst4.low_freq_hz = 40
    vst4.low_gain_db = 18
    
    vst5 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst5.low_freq_hz = 80
    vst5.low_gain_db = 13
    
    vst6 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst6.mid_freq_hz = 2500
    vst6.mid_gain_db = 12
    
    vst7 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst7.high_freq_hz = 8000
    vst7.high_gain_db = 18

    
    vst8 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst8.high_freq_hz = 8000
    vst8.high_gain_db = 18
    
    vst9 = load_plugin("C:\Program Files\Common Files\VST3\OTT.vst3")

    vst9.out_gain_db = 1

    compressioncahin = Pedalboard([
                                NoiseGate(threshold_db=-40, ratio = 10, attack_ms = 2),
                                   vst1,vst2,vst3,
                                   Compressor(threshold_db=-28, ratio=4,attack_ms=20,release_ms=100),
                                   vst4,vst5,vst6,vst7, vst8,
                                   
                                 #  vst9,
                                   
                                   Limiter(threshold_db=-1)
                             
                                   
         
         ])
    ReverbChain = Pedalboard([
         Reverb(room_size=.1, damping=1, wet_level=.05,dry_level=1,width=1)
         ])
     
    Full = Pedalboard([Mix([compressioncahin, ReverbChain])])
    
    effected = Full(audio, samplerate)
    
    with AudioFile((c[0]+ ".wav"), 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)
       
def bassheavyphone():
    vst1 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst1.low_freq_hz = 250
    vst1.low_gain_db = -2
    
    vst2 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst2.low_freq_hz = 500
    vst2.low_gain_db = -2
    
    vst3 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst3.low_freq_hz = 800
    vst3.low_gain_db = -2
    
    vst4 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst4.low_freq_hz = 40
    vst4.low_gain_db = 18
    
    vst5 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst5.low_freq_hz = 80
    vst5.low_gain_db = 13
    
    vst6 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst6.mid_freq_hz = 2500
    vst6.mid_gain_db = 12
    
    vst7 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst7.high_freq_hz = 8000
    vst7.high_gain_db = 18

    
    vst8 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst8.high_freq_hz = 8000
    vst8.high_gain_db = 18
    
    vst9 = load_plugin("C:\Program Files\Common Files\VST3\OTT.vst3")

    vst9.out_gain_db = 1

    compressioncahin = Pedalboard([
                                NoiseGate(threshold_db=-40, ratio = 10, attack_ms = 2),
                                   vst1,vst2,vst3,
                                   Compressor(threshold_db=-20, ratio=3,attack_ms=20,release_ms=100),
                                   vst4,vst5,vst6,vst7, vst8,
                                   
                                 #  vst9,
                                   
                                   Limiter(threshold_db=-1)
                             
                                   
         
         ])
    ReverbChain = Pedalboard([
         Reverb(room_size=.1, damping=1, wet_level=.05,dry_level=1,width=1)
         ])
     
    Full = Pedalboard([Mix([compressioncahin, ReverbChain])])
    
    effected = Full(audio, samplerate)
    
    with AudioFile((c[0]+".wav"), 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)

def musicalphone():
    vst1 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst1.low_freq_hz = 250
    vst1.low_gain_db = -2
    
    vst2 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst2.low_freq_hz = 500
    vst2.low_gain_db = -2
    
    vst3 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst3.low_freq_hz = 800
    vst3.low_gain_db = -2
    
    vst4 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst4.low_freq_hz = 40
    vst4.low_gain_db = 18
    
    vst5 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst5.low_freq_hz = 80
    vst5.low_gain_db = 13
    
    vst6 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst6.mid_freq_hz = 2500
    vst6.mid_gain_db = 12
    
    vst7 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst7.high_freq_hz = 8000
    vst7.high_gain_db = 18

    
    vst8 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst8.high_freq_hz = 8000
    vst8.high_gain_db = 18
    
    vst9 = load_plugin("C:\Program Files\Common Files\VST3\OTT.vst3")

    vst9.out_gain_db = 1

    compressioncahin = Pedalboard([
                                NoiseGate(threshold_db=-40, ratio = 10, attack_ms = 2),
                                   vst1,vst2,vst3,
                                   Compressor(threshold_db=-20, ratio=3,attack_ms=20,release_ms=100),
                                   vst4,vst5,vst6,vst7, vst8,
                                   
                                 #  vst9,
                                   
                                   Limiter(threshold_db=-1)
                             
                                   
         
         ])
    ReverbChain = Pedalboard([
         Reverb(room_size=.1, damping=1, wet_level=.05,dry_level=1,width=1)
         ])
     
    Full = Pedalboard([Mix([compressioncahin, ReverbChain])])
    
    effected = Full(audio, samplerate)
    
    with AudioFile((c[0]+ ".wav"), 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)
        
def techphone():
    vst1 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst1.low_freq_hz = 250
    vst1.low_gain_db = -2
    
    vst2 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst2.low_freq_hz = 500
    vst2.low_gain_db = -2
    
    vst3 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst3.low_freq_hz = 800
    vst3.low_gain_db = -2
    
    vst4 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst4.low_freq_hz = 40
    vst4.low_gain_db = 18
    
    vst5 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst5.low_freq_hz = 80
    vst5.low_gain_db = 13
    
    vst6 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst6.mid_freq_hz = 2500
    vst6.mid_gain_db = 12
    
    vst7 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst7.high_freq_hz = 8000
    vst7.high_gain_db = 18

    
    vst8 = load_plugin("C:\Program Files\Common Files\VST3\TDR VOS SlickEQ.vst3")
    vst8.high_freq_hz = 8000
    vst8.high_gain_db = 18
    
    vst9 = load_plugin("C:\Program Files\Common Files\VST3\OTT.vst3")

    vst9.out_gain_db = 1

    compressioncahin = Pedalboard([
                                NoiseGate(threshold_db=-40, ratio = 10, attack_ms = 2),
                                   vst1,vst2,vst3,
                                   Compressor(threshold_db=-20, ratio=3,attack_ms=20,release_ms=100),
                                   vst4,vst5,vst6,vst7, vst8,
                                   
                                 #  vst9,
                                   
                                   Limiter(threshold_db=-1)
                             
                                   
         
         ])
    ReverbChain = Pedalboard([
         Reverb(room_size=.1, damping=1, wet_level=.05,dry_level=1,width=1)
         ])
     
    Full = Pedalboard([Mix([compressioncahin, ReverbChain])])
    
    effected = Full(audio, samplerate)
    
    with AudioFile((c[0]+ ".wav"), 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)
        

        
if mic:
    if style == "bass":
        bassheavy()
    if style == "music":
        musical()
    if style == "tech":
        tech()
else:
    if style == "bass":
        bassheavyphone()
    if style == "music":
        musicalphone()
    if style == "tech":
        techphone()
# !apt install libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg

# !pip install deepspeech==0.9.3

# !wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm

# !wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer

from deepspeech import Model
import numpy as np
# import os
import wave
# import json

# from IPython.display import Audio

model_file_path = './deepspeech-0.9.3-models.pbmm'
lm_file_path = './deepspeech-0.9.3-models.scorer'
beam_width = 100
lm_alpha = 0.931289039105002
lm_beta = 1.1834137581510284

model = Model(model_file_path)
model.enableExternalScorer(lm_file_path)

model.setScorerAlphaBeta(lm_alpha, lm_beta)
model.setBeamWidth(beam_width)


def read_audio_file(audio_file):
    from subprocess import Popen, PIPE
    print()
    # p=Popen(["ffmpeg", "-y", "-i", "-", "-ar", "16000", "speech.wav"], stdin=audio_file, stdout=PIPE)
    p=Popen(["ffmpeg", "-y", "-i", "speech.ogg", "-ar", "16000", "speech.wav"])
    print()
    p.wait()
    filename = "./speech.wav"
    
    with wave.open(filename, 'rb') as w:
        rate = w.getframerate()
        frames = w.getnframes()
        buffer = w.readframes(frames)
        print("Rates: ", rate)
    return buffer, rate


# from IPython.display import clear_output


def real_time_transcription(audio_file):
    buffer, rate = read_audio_file(audio_file)
    offset = 0
    batch_size = 16384
    text = ''

    stream = model.createStream()

    while offset < len(buffer):
        end_offset = offset + batch_size
        chunk = buffer[offset:end_offset]
        data16 = np.frombuffer(chunk, dtype=np.int16)
        stream.feedAudioContent(data16)
        text = stream.intermediateDecode()
        print(text)
        offset = end_offset
    text = stream.finishStream()
    print(text)
    return text


# Sample File
# !wget -O speech.wav https://github.com/EN10/DeepSpeech/blob/master/man1_wb.wav?raw=true

# !ls

# Audio("speech.wav")

# real_time_transcription("speech.wav")


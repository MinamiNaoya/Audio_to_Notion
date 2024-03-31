from transformers import *
import torch
import soundfile as sf
import os
import torchaudio
from pydub import AudioSegment

device = "cuda:0" if torch.cuda.is_available() else "cpu"

wav2vec2_model_name = "facebook/wav2vec2-large-960h-lv60-self" 
wav2vec2_processor = Wav2Vec2Processor.from_pretrained(wav2vec2_model_name)
wav2vec2_model = Wav2Vec2ForCTC.from_pretrained(wav2vec2_model_name).to(device)

audio_url = ""

def audio_convert(m4a_file):
    wav_filename = m4a_file.replace('m4a', 'wav')
    sound = AudioSegment.from_file(m4a_file, format='m4a')
    sound = sound.export(wav_filename, format='wav')
    return sound

def load_audio(audio_path):
    speech, sr = torchaudio.load(audio_path)
    resampler = torchaudio.transforms.Resample(sr, 16000)
    speech = resampler(speech)
    return speech.squeeze()

def get_transcription_wav2vec2(audio_path, model, processor):
    speech = load_audio(audio_path)
    input_features = processor(speech, return_tensors="pt", sampling_rate=16000)["input_values"].to(device)
    logits = model(input_features)["logits"]
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]
    return transcription.lower()
    
audio_path =  ""

print("###############")
print(get_transcription_wav2vec2(audio_path, wav2vec2_model, wav2vec2_processor))


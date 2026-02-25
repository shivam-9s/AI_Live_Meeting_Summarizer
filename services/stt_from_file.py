import wave
import json
from vosk import Model, KaldiRecognizer

MODEL_PATH = "models/vosk-model-small-en-us-0.15"
AUDIO_FILE = "storage/processed_audio/es2002a_array1_16k.wav"

print("Loading model...")
model = Model(MODEL_PATH)

wf = wave.open(AUDIO_FILE, "rb")

if wf.getnchannels() != 1 or wf.getframerate() != 16000:
    print("Audio must be mono 16k WAV")
    exit(1)

rec = KaldiRecognizer(model, wf.getframerate())

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        print("Partial:", result.get("text"))

final_result = json.loads(rec.FinalResult())
print("\nFinal Transcription:")
print(final_result.get("text"))

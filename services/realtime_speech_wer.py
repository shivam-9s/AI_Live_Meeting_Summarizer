import queue
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer
from jiwer import wer

# Load Vosk model
model = Model("models/vosk-model-small-en-us-0.15")

samplerate = 16000
q = queue.Queue()

# Microphone callback
def callback(indata, frames, time, status):
    q.put(bytes(indata))

rec = KaldiRecognizer(model, samplerate)

print("🎤 Start speaking...")

# Ground truth sentence (for WER comparison)
ground_truth = "hello everyone welcome to the meeting"

transcribed_text = ""

with sd.RawInputStream(samplerate=samplerate, blocksize = 8000, dtype='int16',
                       channels=1, callback=callback):

    while True:
        data = q.get()

        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result.get("text", "")

            if text != "":
                print("🗣 Recognized:", text)

                transcribed_text += " " + text

                # Calculate WER
                error = wer(ground_truth, transcribed_text)

                print("📊 Current WER:", round(error,3))
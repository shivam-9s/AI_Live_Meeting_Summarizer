import os
import wave
import json
from vosk import Model, KaldiRecognizer

MODEL_PATH = "models/vosk-model-small-en-us-0.15"
AUDIO_FOLDER = "storage/processed_audio"
OUTPUT_FOLDER = "storage/transcripts"

model = Model(MODEL_PATH)

for file in os.listdir(AUDIO_FOLDER):

    if file.endswith(".wav"):

        path = os.path.join(AUDIO_FOLDER, file)

        print("\nProcessing:", file)

        wf = wave.open(path, "rb")

        rec = KaldiRecognizer(model, wf.getframerate())

        transcript = ""

        while True:
            data = wf.readframes(4000)

            if len(data) == 0:
                break

            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                transcript += result.get("text", "") + " "

        final_result = json.loads(rec.FinalResult())
        transcript += final_result.get("text", "")

        output_file = os.path.join(
            OUTPUT_FOLDER, file.replace(".wav", ".txt")
        )

        with open(output_file, "w") as f:
            f.write(transcript)

        print("Transcript saved:", output_file)
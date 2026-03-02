import os

from pyannote.audio import Pipeline

AUDIO_FILE = "storage/processed_audio/ES2002a.Array1-01.wav"



print("Loading diarization model...")

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    use_auth_token=os.getenv("HF_TOKEN")
)

print("Running diarization...")

diarization = pipeline(AUDIO_FILE)

for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(f"{turn.start:.2f}s - {turn.end:.2f}s : {speaker}")
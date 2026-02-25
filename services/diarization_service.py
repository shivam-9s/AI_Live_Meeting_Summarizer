from pyannote.audio import Pipeline

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization"
)

audio_file = "storage/processed_audio/es2002a_array1_16k.wav"

diarization = pipeline(audio_file)

for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(f"{turn.start:.1f} → {turn.end:.1f} : {speaker}")
    
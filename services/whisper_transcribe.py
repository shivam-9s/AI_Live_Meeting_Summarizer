import whisper

AUDIO_FILE = "storage/processed_audio/trimmed_30s.wav"

print("Loading Whisper model...")

model = whisper.load_model("base")  
# options: tiny, base, small, medium, large

print("Transcribing audio...")

result = model.transcribe(AUDIO_FILE)

text = result["text"]

print("\nWhisper Transcript:\n")
print(text)

with open("storage/transcripts/whisper_trimmed_30s.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("\nTranscript saved.")
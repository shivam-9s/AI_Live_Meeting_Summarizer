from jiwer import wer

# reference
with open("storage/reference/reference_trimmed.txt", "r", encoding="utf-8") as f:
    reference = f.read().strip().lower()

# vosk transcript
with open("storage/transcripts/trimmed_30s.txt", "r", encoding="utf-8") as f:
    vosk = f.read().strip().lower()

# whisper transcript
with open("storage/transcripts/whisper_trimmed_30s.txt", "r", encoding="utf-8") as f:
    whisper = f.read().strip().lower()


print("\nREFERENCE:\n", reference[:200])
print("\nVOSK:\n", vosk)
print("\nWHISPER:\n", whisper)

print("\n------------------------")

vosk_wer = wer(reference, vosk)
whisper_wer = wer(reference, whisper)

print("VOSK WER:", vosk_wer)
print("WHISPER WER:", whisper_wer)

print("\nBetter Model:", "Whisper" if whisper_wer < vosk_wer else "Vosk")
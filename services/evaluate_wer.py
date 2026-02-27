from jiwer import wer

# Load reference transcript
with open("storage/reference/reference_trimmed.txt", "r", encoding="utf-8") as f:
    reference = f.read().strip().lower()

# Load hypothesis transcript
with open("storage/transcripts/trimmed_30s.txt", "r", encoding="utf-8") as f:
    hypothesis = f.read().strip().lower()

print("\nReference:\n", reference[:200])
print("\nHypothesis:\n", hypothesis)

error = wer(reference, hypothesis)

print("\nWord Error Rate:", error)
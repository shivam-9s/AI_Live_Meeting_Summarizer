from jiwer import wer

# Load reference transcript (correct text)
with open("storage/reference.txt", "r") as f:
    reference = f.read()

# Load model transcript
with open("storage/transcripts/es2002a_array1_16k.txt", "r") as f:
    hypothesis = f.read()

# Calculate WER
error = wer(reference, hypothesis)

print("Word Error Rate:", error)
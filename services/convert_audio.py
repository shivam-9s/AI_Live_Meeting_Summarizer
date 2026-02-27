import librosa
import soundfile as sf

INPUT_FILE = "storage/raw_audio/ES2002a.Array1-01.wav"
OUTPUT_FILE = "storage/processed_audio/trimmed_30s.wav"

print("Loading audio...")

audio, sr = librosa.load(INPUT_FILE, sr=16000, mono=True)

print("Trimming first 30 seconds...")

audio_trimmed = audio[0:30*16000]

print("Saving audio...")

sf.write(OUTPUT_FILE, audio_trimmed, 16000, subtype='PCM_16')

print("Audio converted successfully!")
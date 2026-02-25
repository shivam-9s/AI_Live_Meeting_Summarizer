import librosa
import soundfile as sf

INPUT_FILE = "storage/raw_audio/ES2002a.Array1-01.wav"
OUTPUT_FILE = "storage/processed_audio/es2002a_array1_16k.wav"

print("Loading audio...")

audio, sr = librosa.load(INPUT_FILE, sr=16000, mono=True)

print("Converted sample rate:", sr)

sf.write(OUTPUT_FILE, audio, 16000)

print("Converted file saved.")
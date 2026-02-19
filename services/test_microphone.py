import sounddevice as sd

DEVICE_INDEX = 9  # your device

info = sd.query_devices(DEVICE_INDEX)
print(info)

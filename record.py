import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # qualidade do áudio
seconds = 4

print("Gravando...")
audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

write("data/maria/audio1.wav", fs, audio)
print("Salvo!")
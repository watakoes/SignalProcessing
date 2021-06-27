import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

path = 'ff_A.wav'
data, samplerate = sf.read(path)

t = np.arange(0, len(data)) / samplerate

plt.plot(t, data)
plt.show()
plt.close()
import sounddevice as sd
import numpy as np
import time
import os
from scipy.fft import fft, fftfreq

# ==== CONFIGURATION ====
DEVICE_INDEX = 2                    
FS = 48000                          
DURATION = 10                        
FRAME_SIZE = 2048                    
CLAP_THRESHOLD = 0.01               
CLAP_INTERVAL = 0.5                  
EXPECTED_FREQ_RANGE = (500, 4000)    


def detect_claps():
    print(f"Using microphone device index: {DEVICE_INDEX}")
    print("Listening for 10 seconds...")
    claps = []
    last_clap_time = 0

    def callback(indata, frames, time_info, status):
        nonlocal last_clap_time
        audio = indata[:, 0]

        # Amplitude calculation (RMS)
        amplitude = np.sqrt(np.mean(audio**2))
        print(f"Amplitude: {amplitude:.2f}")

        if amplitude > CLAP_THRESHOLD:
            # FFT to get dominant frequency
            yf = fft(audio)
            freqs = fftfreq(len(yf), 1 / FS)
            magnitude = np.abs(yf[:len(yf)//2])
            freqs = freqs[:len(yf)//2]
            dominant_freq = freqs[np.argmax(magnitude)]

            print(f"Dominant Frequency: {dominant_freq:.2f} Hz")

            # Validate frequency range
            if EXPECTED_FREQ_RANGE[0] <= dominant_freq <= EXPECTED_FREQ_RANGE[1]:
                now = time_info.inputBufferAdcTime
                if now - last_clap_time > CLAP_INTERVAL:
                    claps.append(now)
                    last_clap_time = now
                    print(f"👏 Valid clap detected at {now:.2f}s")
            else:
                print(f"❌ Ignored: {dominant_freq:.2f} Hz not in range")

    try:
        with sd.InputStream(callback=callback, channels=1, samplerate=FS,
                            blocksize=FRAME_SIZE, device=DEVICE_INDEX):
            sd.sleep(int(DURATION * 1000))
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

    print(f"Total claps detected: {len(claps)}")
    return claps


# ==== MAIN LOOP ====
if __name__ == "__main__":
    print("Clap detection started. Press Ctrl+C to stop.")
    try:
        while True:
            claps = detect_claps()
            num_claps = len(claps)

            if num_claps == 1:
                print("▶️ One clap — PLAY (YouTube)")
                os.system("xdotool key k")  # YouTube play/pause
            elif num_claps == 2:
                print("⏸️ Two claps — PAUSE (YouTube)")
                os.system("xdotool key space")  # Alt YouTube pause
            else:
                print("No valid clap pattern detected.")

            time.sleep(1)
    except KeyboardInterrupt:
        print("Detection stopped by user.")

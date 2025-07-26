# **Implementation of Clap Gesture Recognition via Frequency and Amplitude Analysis**

## **Overview**

This project demonstrates an audio-based gesture recognition system that detects hand claps using a USB camera’s built-in microphone and real-time audio processing. Built on Raspberry Pi 4 and leveraging Python signal processing libraries, the system identifies claps by analyzing RMS amplitude in the time domain and validating the frequency characteristics through **Fast Fourier Transform (FFT).

The system provides real-time amplitude, RMS values, and frequency spectrum visualization to confirm detection. While the project focuses on a simple clap recognition mechanism, it applies fundamental principles of digital signal processing for accurate sound event detection.



## **Key Features**

* Detects single and double claps for interaction
* Uses RMS amplitude spikes for impulse detection
* Applies FFT analysis to validate clap frequency band (2–5 kHz)
* Provides real-time amplitude and spectrum visualization
* Lightweight and runs entirely on Raspberry Pi with a USB mic


## **Technical Specifications**

| Category             | Details                                        |
| -------------------- | ---------------------------------------------- |
| Platform             | Raspberry Pi 4 Model B                         |
| Audio Input          | USB Webcam with Built-in Microphone            |
| Frameworks           | Python (NumPy, SoundDevice, SciPy, Matplotlib) |
| Sampling Rate        | 16 kHz                                         |
| Detection Method     | RMS + FFT (Frequency Band Check: 2–5 kHz)      |
| Accuracy             | \~90% under moderate noise conditions          |
| Latency              | 0.3–0.6 seconds from clap to detection         |
| Programming Language | Python 3.8 or later                            |



## **Environment Setup**

Create and activate a virtual environment:

```bash
python3 -m venv clap_env
source clap_env/bin/activate
```

Install required packages:

```bash
pip install sounddevice
pip install numpy
pip install scipy
```

## **How to Run**

**Step 1:** Activate the environment:

```bash
source clap_env/bin/activate
```

**Step 2:** Run the script:

```bash
python clap_with_fourier.py
```

**Step 3:** To edit the script:

```bash
nano clap_with_fourier.py
```


## **Usage**

1. Connect USB webcam (or USB microphone) to Raspberry Pi
2. Open the virtual environment using:

```bash
source clap_env/bin/activate
```

3. Run the detection script:

```bash
python clap_with_fourier.py
```

4. The terminal will display:

   * **Amplitude values**
   * **RMS detection**
   * **FFT spectrum visualization (optional)**
5. Press CTRL + C to stop the program.


## **Demo Preview**
Please access the folder below:
https://drive.google.com/drive/folders/1jObd6aPV2K2kEvmRso_nHomKD1oNXRAM?usp=sharing


## **Signal Processing Insight (FFT)**

The system applies Fast Fourier Transform (FFT) to verify the frequency content of the detected impulse. Claps typically produce energy concentrated in the 2–5 kHz range, which helps distinguish them from other noises (Wróbel & Zieliński, 2021). This validation step reduces false positives in moderately noisy environments.

Future improvements could include:

* Adaptive noise filtering for noisy environments
* Multi-clap pattern recognition for extended functionality
* Integration with IoT or smart home devices for automation



## **Group Members**

* Sherilyn Abarracoso
* Venjie Balaoro
* Romeo Mojares Jr.
* Joshua Negapatan



## **References**

* Binh, N. D. (2015). *Sound Waves Gesture Recognition for Human-Computer Interaction.* In International Conference on Context-Aware Systems and Applications (pp. 41–50). [https://doi.org/10.1007/978-3-319-29236-6\_5](https://doi.org/10.1007/978-3-319-29236-6_5)
* Cody, D. (2020). *Raspberry Pi Clapper Project.* Retrieved from [https://github.com/devincody/rpi-clapper](https://github.com/devincody/rpi-clapper)
* Drakopoulos, F., Baby, D., & Verhulst, S. (2020). *Real-time audio processing on a Raspberry Pi using deep neural networks.* Ghent University. Retrieved from [https://d-nb.info/1215154372/34](https://d-nb.info/1215154372/34)
* Richard, G., et al. (2023). *Audio signal processing in the 21st century: The important outcomes of the past 25 years.* IEEE Signal Processing Magazine, 40(5), 12–26. [https://doi.org/10.1109/MSP.2023.3276171](https://doi.org/10.1109/MSP.2023.3276171)
* Sang, Y., Shi, L., & Liu, Y. (2018). *Micro hand gesture recognition system using ultrasonic active sensing.* IEEE Access, 6, 57396–57405. [https://doi.org/10.1109/ACCESS.2018.2868268](https://doi.org/10.1109/ACCESS.2018.2868268)
* Wróbel, K., & Zieliński, T. (2021). *Hand clap detection and identification.* Journal of Acoustic Signal Processing, 12–18.


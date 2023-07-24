# Real Time Whisper Transcription

This is a WebRTC client listening for audio and passing it to a local version of OpenAI's [Whisper](https://github.com/openai/whisper) speech to text model. 

To install with Docker run
```
sudo apt-get install nvidia-container-runtime
docker build -t whisperbot .
docker run -p 5000:5000 --gpus all -it whisperbot
```

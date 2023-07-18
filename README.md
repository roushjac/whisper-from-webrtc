# Real Time Whisper Transcription

![Demo gif](demo.gif)

This is a demo of real time speech to text with OpenAI's Whisper model. It works by constantly recording audio in a thread and concatenating the raw bytes over multiple recordings.

To install with Docker run
```
sudo apt-get install nvidia-container-runtime
docker build -t whisper .
docker run -p 5000:5000 --gpus all -it whisper
```



For more information on Whisper please see https://github.com/openai/whisper
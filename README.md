# Discord Real Time Whisper Transcription

This is a Discord bot using a real time speech to text model from OpenAI called Whisper. It works by constantly recording audio in a thread and concatenating the raw bytes over multiple recordings. It then transcribes the speech of all users in a channel.

To install with Docker run
```
sudo apt-get install nvidia-container-runtime
docker build -t whisperbot .
docker run -p 5000:5000 --gpus all -it whisperbot
```

For more information on Whisper please see https://github.com/openai/whisper
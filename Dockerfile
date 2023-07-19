FROM pytorch/pytorch

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get install -y software-properties-common && \
    apt-get install -y git && \
    apt-get install -y ffmpeg && \
    apt-get install -y portaudio19-dev && \
    apt-get install -y python3-pyaudio

# RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE 5000

# CMD ["python3", "transcribe.py"]
FROM pytorch/pytorch

# removes any manual inputs from installations
ENV DEBIAN_FRONTEND noninteractive

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# copy .gitconfig to root since Docker user is root
# COPY .gitconfig /root/

# install dependencies
RUN apt-get update 
RUN apt-get install -y build-essential
RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y software-properties-common
RUN apt-get install -y ffmpeg
RUN apt-get install -y portaudio19-dev
RUN apt-get install -y python3-pyaudio
RUN apt-get install -y git

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# CMD ["python3", "transcribe.py"]
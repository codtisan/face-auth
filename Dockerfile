FROM python:3.10-slim

WORKDIR /usr/src/app

COPY . .

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libhdf5-dev \
    pkg-config \
    ffmpeg \ 
    libsm6 \
    libxext6

RUN pip install --upgrade pip setuptools wheel

RUN pip install -r requirements.txt

EXPOSE 3000

RUN chmod +x scripts/entrypoint.sh

ENTRYPOINT [ "scripts/entrypoint.sh" ] 
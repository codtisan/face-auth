FROM python:3.10-slim

WORKDIR /usr/src/app

COPY . .

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    python3-dev \
    libhdf5-dev \
    pkg-config \
    ffmpeg \ 
    libsm6 \
    libxext6

ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

RUN pip install --upgrade pip setuptools wheel

RUN /root/.cargo/bin/uv pip install --system --no-cache -r requirements.txt

EXPOSE 3000

RUN chmod +x scripts/entrypoint.sh

ENTRYPOINT [ "scripts/entrypoint.sh" ] 
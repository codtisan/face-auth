FROM python:3.10-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip

RUN pip install --no-binary h5py h5py

RUN pip install -r --no-cache-dir requirements.txt

EXPOSE 3000

CMD [ "python3", "main.py" ]
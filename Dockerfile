FROM python:3.10-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 3000

RUN chmod +x scripts/entrypoint.sh

ENTRYPOINT [ "scripts/entrypoint.sh" ] 
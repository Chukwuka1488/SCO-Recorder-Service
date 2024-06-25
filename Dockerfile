FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

# Install curl and libgl1-mesa-dev
# Install curl, libgl1-mesa-dev, and libglib2.0-0
RUN apt-get update && apt-get install -y curl libgl1-mesa-dev libglib2.0-0
COPY src src

EXPOSE 7100

HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 CMD curl --fail http://localhost:7100/health || exit 1

ENTRYPOINT ["python", "./src/app.py"]

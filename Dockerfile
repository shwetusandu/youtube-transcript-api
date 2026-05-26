FROM apify/actor-python:3.11

COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt && \
    apt-get update && apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*

COPY . ./

CMD ["python", "main.py"]

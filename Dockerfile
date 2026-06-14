FROM python:3.11-slim

# Create working directory
WORKDIR /app

# Copy Python files
COPY main.py extractzip.py countfiles.py /app/

# Copy data folder (ZIP + manifest)
COPY data /data

# Install dependencies (if any)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt || true

# Default command
CMD ["python", "main.py"]

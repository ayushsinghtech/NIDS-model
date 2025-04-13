# Dockerfile
FROM python:3.9-slim

# Install system dependencies including packet processing tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    tcpdump \
    libpcap-dev \
    python3-dev
# Set the working directory inside the container
WORKDIR /app

# Copy application code and dependency files
COPY app/ ./app/
COPY run.py .
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create directories for data and models if not present
RUN mkdir -p /data /models

# Expose port 5000 for Flask
EXPOSE 5000

# Run the Flask app
CMD ["python", "run.py"]

# Use official Python runtime
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install build dependencies for compiling packages like psutil
RUN apt-get update && \
    apt-get install -y gcc python3-dev libffi-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy dependencies
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project code
COPY . .

# Expose port Cloud Run will use
ENV PORT=8080
EXPOSE 8080

# Run FastAPI server
CMD ["python", "service_coordinator_agent/server.py"]
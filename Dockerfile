FROM debian:buster-slim

# Update package lists
RUN apt-get update && apt-get upgrade -y

# Install required packages
RUN apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libpq-dev

# Clean up
RUN rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

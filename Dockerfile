# Use a more recent base image (e.g., Ubuntu 20.04)
FROM ubuntu:20.04

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Rest of your Dockerfile instructions...

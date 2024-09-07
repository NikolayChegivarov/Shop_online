# Stage 1: Create a custom image with Ubuntu sources and GPG keys
FROM ubuntu:20.04 AS ubuntu-source

# Copy necessary files from Ubuntu repository
COPY --from=ubuntu:20.04 /etc/apt/sources.list /etc/apt/sources.list
COPY --from=ubuntu:20.04 /etc/apt/trusted.gpg.d/ubuntu-keyring.gpg /etc/apt/trusted.gpg.d/

# Exit stage 1
EXIT 0

# Stage 2: Use the custom image as a base
FROM debian:buster-slim

# Set working directory
WORKDIR /app

# Update package lists
RUN apt-get update && apt-get upgrade -y

# Install system dependencies
RUN apt-get install -y \
    build-essential \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy application code
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

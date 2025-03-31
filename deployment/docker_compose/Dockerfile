# Use official Python base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy application files
COPY backend/ /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements/default.txt

# Expose ports for both services
EXPOSE 8000 8001

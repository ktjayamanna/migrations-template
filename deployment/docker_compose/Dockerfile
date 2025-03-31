# Use official Python base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy application files
COPY backend/ /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements/default.txt

# Run the application
CMD ["uvicorn", "bitly.server.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

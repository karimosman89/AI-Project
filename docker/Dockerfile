# Base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY src/ .

# Expose the Flask API port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
